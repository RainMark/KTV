#!/usr/python3


import sys
import os
import lib.mysql


class ktv_server(object):
    def __init__(self, user, password, database):
        svr_db = mdb(user, password, database)

    def svr_top100(self):
        self.svr_db.top100()

