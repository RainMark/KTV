#!/usr/python3

from flask import Flask
from flask import request
from flask import Response
from lib.server import ktv_server

ktv = Flask(__name__)
svr = ktv_server(user='root', password='root', database='ktv_db')

@ktv.route('/top/<top_type>', methods=['GET'])
def top_handler(top_type):
    print('Get Top %s' % (top_type))
    top_list_dumps = svr.svr_get_top()
    print(top_list_dumps)
    resp = Response(response=top_list_dumps, status=200, mimetype="application/json")
    return resp

@ktv.route('/playing/fetch/<int:cid>', methods=['GET'])
def playing_list_fetch_handler(cid):
    print('Fetching Playing list..')
    playing_list_dumps = svr.svr_playing_list_fetch(cid)
    resp = Response(response=playing_list_dumps, status=200, mimetype="application/json")
    return resp

@ktv.route('/playing/<ope>/<cid>/<sid>', methods=['GET'])
def playing_list_operations_handler(ope, cid, sid):
    if 'add' == ope:
        result = svr.svr_playing_list_add(cid, sid)
    elif 'delete' == ope:
        result = svr.svr_playing_list_delete(cid, sid)
    else:
        result = 'Invalid URL.'

    resp = Response(response=result, status=200, mimetype="application/json")
    return resp

if __name__ == '__main__':
    ktv.run()
