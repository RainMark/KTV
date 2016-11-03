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

if __name__ == '__main__':
    ktv.run()
