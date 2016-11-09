#!/usr/python3

import sys
import os
import json
from lib.database import stv_mariadb


class stv_server(object):
    def __init__(self, user, password, database):
        self.db = stv_mariadb(user, password, database)

    def top_fetch(self, top_type='all'):
        top_list = self.db.hot_all()
        return json.dumps(top_list)

    def playing_list_fetch(self, client_id):
        playing_list = self.db.playing_list_fetch(client_id)
        # print(playing_list)
        return json.dumps(playing_list)

    def playing_list_add(self, client_id, song_id):
        # print(client_id, " ", song_id)
        if True == self.db.playing_list_add(client_id, song_id):
            retval = (('Insert OK'))
        else:
            retval = (('Insert Failed'))

        return json.dumps(retval)

    def playing_list_delete(self, client_id, song_id):
        # print(client_id, " ", song_id)
        if True == self.db.playing_list_delete(client_id, song_id):
            retval = (('Delete OK'))
        else:
            retval = (('Delete Failed'))

        return json.dumps(retval)

    def playing_list_resort(self, client_id, song_id, order):
        # print(client_id, " ", song_id)
        if True == self.db.playing_list_resort(client_id, song_id, order):
            retval = (('Resort OK'))
        else:
            retval = (('Resort Failed'))

        return json.dumps(retval)

    def search_singer(self, key, use_abridge):
        if use_abridge:
            return json.dumps(self.db.search_singer_by_abridge(key))
        else:
            return json.dumps(self.db.search_singer_by_fullname(key))

    def search_song(self, key, use_abridge):
        if use_abridge:
            return json.dumps(self.db.search_song_by_abridge(key))
        else:
            return json.dumps(self.db.search_song_by_fullname(key))
