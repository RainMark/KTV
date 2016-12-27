#!/usr/python3

import logging
import json
import sys
import os
from flask import Flask
from flask import request
from flask import Response
from flask import send_file
from flask_cors import CORS

LIBS = '/var/lib/stv'

sys.path.append(os.path.join(os.getcwd(), 'lib'))
from server import stv_server

stv = Flask(__name__)
CORS(stv)

svr = stv_server(user='root', password='root', database='stv_db')
logging.basicConfig(level=logging.WARNING)

# Common handler
@stv.route('/top/<top_type>', methods=['GET'])
def top_handler(top_type):
    dump = svr.top_fetch(top_type)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/search/<srh_method>/<srh_type>/<srh_key>', methods=['GET'])
def search_handler(srh_method, srh_type, srh_key):
    dump = json.dumps([])
    use_abridge = ('abbreviation' == srh_method)
    if 'singer' == srh_type:
        dump = svr.search_singer(srh_key, use_abridge)
    elif 'song' == srh_type:
        dump = svr.search_song(srh_key, use_abridge)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/singer/fetch/<int:id>', methods=['GET'])
def singer_song_fetch(id):
    dump = svr.singer_song_fetch(id)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/download/mv/<int:id>', methods=['GET'])
def video_download_handler(id):
    video = os.path.join(os.path.join(LIBS, 'mv'), str(id))
    try:
        return send_file(video)
    except Exception as e:
        logging.error(e)
        return str('NULL')

@stv.route('/download/album/<int:id>', methods=['GET'])
def album_download_handler(id):
    pic  = os.path.join(os.path.join(LIBS, 'singer'), str(id))
    try:
        return send_file(pic)
    except Exception as e:
        logging.error(e)
        return str('NULL')

@stv.route('/comment/fetch/<int:id>', methods=['GET'])
def comment_fetch_handler(id):
    dump = svr.comment_fetch(id)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/comment/<int:id>', methods=['POST'])
def comment_handler(id):
    logging.error(request.form)
    if None == request.form.get('content'):
        dump = json.dumps('Failed')
    else:
        dump = svr.comment_insert(id, request.form['content'])
    return Response(response=dump, status=200, mimetype="application/json")

# include machine ID.
@stv.route('/praise/fetch/<int:seq>/<int:cid>/<int:sid>', methods=['GET'])
def praise_fetch_handler(seq, cid, sid):
    dump = json.dumps('Failed')
    logging.debug('%s %s %s' % (seq, cid, sid))
    if svr.check_seq(cid, seq):
        dump = svr.praise_fetch(cid, sid)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/praise/increase/<int:seq>/<int:cid>/<int:sid>', methods=['GET'])
def praise_increase_handler(seq, cid, sid):
    dump = json.dumps('Failed')
    if svr.check_seq(cid, seq):
        dump = svr.praise_increase(cid, sid)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/network/check/<int:seq>/<int:id>', methods=['GET'])
def network_check_handler(seq, id):
    if svr.check_seq(id, seq):
        resp = json.dumps('Online')
    else:
        resp = json.dumps('Offline')
    return Response(response=resp, status=200, mimetype="application/json")

@stv.route('/sequence/init/<int:machine>/<int:seq>', methods=['GET'])
def sequence_init_handler(machine, seq):
    svr.insert_seq(machine, seq)
    return Response(response=json.dumps('OK'), status=200, mimetype="application/json")

@stv.route('/playcontrol/insert/<instruction>/<int:seq>/<int:id>', methods=['GET'])
def playcontrol_insert_handler(instruction, seq, id):
    dump = json.dumps('Failed')
    if svr.check_seq(id, seq):
        if instruction in ['play', 'pause', 'next']:
            dump = svr.instruction_push(id, instruction)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/playcontrol/fetch/<int:seq>/<int:id>', methods=['GET'])
def playcontrol_fetch_handler(seq, id):
    dump = json.dumps([])
    if svr.check_seq(id, seq):
        dump = svr.instruction_popall(id)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/playlist/fetch/<int:seq>/<int:id>', methods=['GET'])
def playlist_fetch_handler(seq, id):
    dump = json.dumps([])
    if svr.check_seq(id, seq):
        dump = svr.playing_list_fetch(id)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/history/fetch/<int:seq>/<int:id>', methods=['GET'])
def history_list_fetch_handler(seq, id):
    dump = json.dumps([])
    if svr.check_seq(id, seq):
        dump = svr.history_list_fetch(id)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/playlist/<operation>/<int:seq>/<int:cid>/<int:sid>', methods=['GET'])
def playlist_operation_handler(operation, seq, cid, sid):
    dump = json.dumps([])
    if svr.check_seq(cid, seq):
        if 'add' == operation:
            dump = svr.playing_list_add(cid, sid)
        elif 'delete' == operation:
            dump = svr.playing_list_delete(cid, sid)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/playlist/resort/<int:seq>/<int:cid>/<int:sid>/<int:order>', methods=['GET'])
def playlist_resort_handler(seq, cid, sid, order):
    dump = json.dumps([])
    if svr.check_seq(cid, seq):
        dump = svr.playing_list_resort(cid, sid, order)
    return Response(response=dump, status=200, mimetype="application/json")

@stv.route('/recommendation/<int:seq>/<int:id>', methods=['GET'])
def recommendation_fetch_handler(seq, id):
    dump = json.dumps([])
    if svr.check_seq(id, seq):
        dump = svr.recommendation_fetch(str(id))
    return Response(response=dump, status=200, mimetype="application/json")

if __name__ == '__main__':
    stv.run(host = '0.0.0.0')
