#!/usr/python3

from flask import Flask
from flask import request
import lib.server
import lib.recommend
import lib.mysql

ktv = Flask(__name__)
svr = server(user='root', password='root', database='ktv_db')

@ktv.route('/hot100', methods=['GET'])
def hot100():
    print('hot100')
    pass

if __name__ == '__main__':
    ktv.run()
