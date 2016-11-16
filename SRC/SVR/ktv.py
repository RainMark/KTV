#!/usr/python3

import json
import sys
import os
from flask import Flask
from flask import request
from flask import Response
# sys.path.append(os.path.abspath(os.path.curdir) + "/lib")
sys.path.append(os.path.join(os.getcwd(), 'lib'))
from server import stv_server


stv = Flask(__name__)
svr = stv_server(user='root', password='root', database='stv_db')

@stv.route('/top/<top_type>', methods=['GET'])
def top_handler(top_type):
    print('Get Top %s' % (top_type))
    top_list_dumps = svr.top_fetch()
    resp = Response(response=top_list_dumps, status=200, mimetype="application/json")
    return resp

@stv.route('/playing/fetch/<int:cid>', methods=['GET'])
def playing_list_fetch_handler(cid):
    print('Fetching Playing list..')
    playing_list_dumps = svr.playing_list_fetch(cid)
    resp = Response(response=playing_list_dumps, status=200, mimetype="application/json")
    return resp

@stv.route('/playing/<ope>/<int:cid>/<int:sid>', methods=['GET'])
def playing_list_operations_handler(ope, cid, sid):
    if 'add' == ope:
        result = svr.playing_list_add(cid, sid)
    elif 'delete' == ope:
        result = svr.playing_list_delete(cid, sid)
    else:
        result = json.dump((('Invalid Request.')))

    resp = Response(response=result, status=200, mimetype="application/json")
    return resp

@stv.route('/playing/resort/<int:cid>/<int:sid>/<int:order>', methods=['GET'])
def playing_list_resort_handler(cid, sid, order):
    print('Resorting Playing list..')
    result = svr.playing_list_resort(cid, sid, order)
    resp = Response(response=result, status=200, mimetype="application/json")
    return resp

@stv.route('/search/<srh_method>/<srh_type>/<srh_key>', methods=['GET'])
def search_handler(srh_method, srh_type, srh_key):
    use_abridge = ('abbreviation' == srh_method)
    if 'singer' == srh_type:
        result = svr.search_singer(srh_key, use_abridge)

    elif 'song' == srh_type:
        result = svr.search_song(srh_key, use_abridge)

    else:
        result = json.dump((()))

    resp = Response(response=result, status=200, mimetype="application/json")
    return resp

if __name__ == '__main__':
    stv.run(host = '0.0.0.0')
