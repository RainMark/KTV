#!/usr/python3

import json
import sys
import os
from flask import Flask
from flask import request
from flask import Response
from flask import send_file

LIBS = '/var/lib/stv'

sys.path.append(os.path.join(os.getcwd(), 'lib'))
from server import stv_server


stv = Flask(__name__)
svr = stv_server(user='root', password='root', database='stv_db')

# Common handler
@stv.route('/top/<top_type>', methods=['GET'])
def top_handler(top_type):
    dumps = svr.top_fetch(top_type)
    return Response(response=dumps, status=200, mimetype="application/json")

@stv.route('/search/<srh_method>/<srh_type>/<srh_key>', methods=['GET'])
def search_handler(srh_method, srh_type, srh_key):
    use_abridge = ('abbreviation' == srh_method)
    if 'singer' == srh_type:
        result = svr.search_singer(srh_key, use_abridge)

    elif 'song' == srh_type:
        result = svr.search_song(srh_key, use_abridge)

    else:
        result = json.dumps((()))

    return Response(response=result, status=200, mimetype="application/json")

@stv.route('//singer/fetch/<int:sid>', methods=['GET'])
def singer_song_fetch(sid):
    dumps = svr.singer_song_fetch(sid)
    return Response(response=dumps, status=200, mimetype="application/json")

@stv.route('/download/mv/<int:sid>', methods=['GET'])
def video_download_handler(sid):
    video = os.path.join(os.path.join(LIBS, 'mv'), str(sid))
    try:
        return send_file(video)
    except Exception as e:
        print(e)
        return str('NULL')

@stv.route('/download/album/<int:sid>', methods=['GET'])
def album_download_handler(sid):
    pic  = os.path.join(os.path.join(LIBS, 'singer'), str(sid))
    try:
        return send_file(pic)
    except Exception as e:
        print(e)
        return str('NULL')

@stv.route('/comment/fetch/<int:sid>/', methods=['GET'])
def comment_fetch_handler(sid):
    comment = svr.comment_fetch(sid)
    return Response(response=comment, status=200, mimetype="application/json")

# Desktop handler
@stv.route('/desktop/playing/fetch/<int:cid>', methods=['GET'])
def desktop_playing_list_fetch_handler(cid):
    playing_list_dumps = svr.playing_list_fetch(cid)
    return Response(response=playing_list_dumps, status=200, mimetype="application/json")

@stv.route('/desktop/history/fetch/<int:cid>', methods=['GET'])
def desktop_history_list_fetch_handler(cid):
    history_list_dumps = svr.history_list_fetch(cid)
    return Response(response=history_list_dumps, status=200, mimetype="application/json")

@stv.route('/desktop/playing/<ope>/<int:cid>/<int:sid>', methods=['GET'])
def desktop_playing_list_operations_handler(ope, cid, sid):
    if 'add' == ope:
        result = svr.playing_list_add(cid, sid)
    elif 'delete' == ope:
        result = svr.playing_list_delete(cid, sid)
    else:
        result = json.dumps((('Invalid Request.')))

    return Response(response=result, status=200, mimetype="application/json")

@stv.route('/desktop/playing/resort/<int:cid>/<int:sid>/<int:order>', methods=['GET'])
def desktop_playing_list_resort_handler(cid, sid, order):
    result = svr.playing_list_resort(cid, sid, order)
    return Response(response=result, status=200, mimetype="application/json")

@stv.route('/desktop/insert/<int:cid>/<int:seq>', methods=['GET'])
def desktop_sequence_init_handler(cid, seq):
    svr.insert_seq(cid, seq)
    return Response(response=json.dumps('OK'), status=200, mimetype="application/json")

@stv.route('/desktop/recommendation/<int:cid>', methods=['GET'])
def desktop_recommendation_fetch_handler(cid):
    dumps = svr.recommendation_fetch(str(cid))
    return Response(response=dumps, status=200, mimetype="application/json")

# App handler
@stv.route('/app/check/<int:cid>/<int:seq>', methods=['GET'])
def app_network_check_handler(cid, seq):
    retval = svr.check_seq(cid, seq)
    if retval:
        result = json.dumps('Online')
    else:
        result = json.dumps('Offline')

    return Response(response=result, status=200, mimetype="application/json")

@stv.route('/app/playing/<ope>/<int:seq>/<int:cid>/<int:sid>', methods=['GET'])
def app_playing_list_operations_handler(ope, seq, cid, sid):
    retval = svr.check_seq(cid, seq)
    if not retval:
        result = json.dumps((('Offline')))
    elif 'add' == ope:
        result = svr.playing_list_add(cid, sid)
    elif 'delete' == ope:
        result = svr.playing_list_delete(cid, sid)
    else:
        result = json.dumps((('Invalid Request.')))

    return Response(response=result, status=200, mimetype="application/json")

@stv.route('/app/playing/fetch/<int:seq>/<int:cid>', methods=['GET'])
def app_playing_list_fetch_handler(seq, cid):
    retval = svr.check_seq(cid, seq)
    if not retval:
        result = json.dumps((('Offline')))
    else:
        result = svr.playing_list_fetch(cid)

    return Response(response=result, status=200, mimetype="application/json")

if __name__ == '__main__':
    stv.run(host = '0.0.0.0')
