#!/usr/python3

import sys
import os
import json
from lib.database import mdb as ktv_db


class ktv_server(object):
    def __init__(self, user, password, database):
        self.svr_db = ktv_db(user, password, database)

    def svr_get_top(self, top_type='all'):
        top_list = self.svr_db.hot_all()
        return json.dumps(top_list)

