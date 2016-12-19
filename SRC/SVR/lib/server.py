#!/usr/python3

import json, logging
from database import stv_mariadb
from recommendation import recommend as stv_rd

class stv_server(object):
    def __init__(self, user, password, database):
        self.db = stv_mariadb(user, password, database)
        self.rd = stv_rd(self.db)
        self.rd.train_set()
        self.rd.item_similarity()
        self.sequences = dict()
        self.praise = dict()

    def check_seq(self, cid, seq):
        if None == self.sequences.get(cid):
            return False

        if seq == self.sequences[cid]:
            return True
        else:
            return False

    def insert_seq(self, cid, seq):
        self.sequences[cid] = seq

    def top_fetch(self, top_type='hotall'):
        if 'random' == top_type:
            top_list = self.db.song_fetch_by_random()
            for v in top_list:
                print(v)
        elif 'comment' == top_type:
            top_list = self.db.song_fetch_by_most_comment()
            for v in top_list:
                print(v)
        else:
            top_list = self.db.hot_fetch(top_type)
        return json.dumps(top_list[0:50])

    def recommendation_fetch(self, client_id):
        rd_list = self.rd.do_recommend(client_id, 50)
        for v in rd_list:
            print(v)
        return json.dumps(rd_list)

    def comment_fetch(self, sid):
        return json.dumps(self.db.comment_fetch(sid)[0:20])

    def praise_fetch(self, cid, sid):
        dump = json.dumps({sid: 0})
        logging.debug(dump)
        if self.praise.get(cid):
            if self.praise[cid].get(sid):
                dump = json.dumps(self.praise[cid])
        logging.debug(dump)
        return dump

    def praise_increase(self, cid, sid):
        if None == self.praise.get(cid):
            self.praise[cid] = dict()
            self.praise[cid][sid] = 1
        elif None == self.praise[cid].get(sid):
            self.praise[cid][sid] = 1
        else:
            self.praise[cid][sid] += 1
        return json.dumps('Success')

    def playing_list_fetch(self, client_id):
        playing_list = self.db.playing_list_fetch(client_id)
        # print(playing_list)
        return json.dumps(playing_list)

    def history_list_fetch(self, client_id):
        playing_list = self.db.history_list_fetch(client_id)
        # print(playing_list)
        return json.dumps(playing_list)

    def playing_list_add(self, client_id, song_id):
        # print(client_id, " ", song_id)
        if self.db.playing_list_add(client_id, song_id):
            retval = 'Success'
        else:
            retval = 'Failed'
        return json.dumps(retval)

    def playing_list_delete(self, client_id, song_id):
        # print(client_id, " ", song_id)
        if self.db.playing_list_delete(client_id, song_id):
            retval = 'Success'
        else:
            retval = 'Failed'
        return json.dumps(retval)

    def playing_list_resort(self, client_id, song_id, order):
        # print(client_id, " ", song_id)
        if self.db.playing_list_resort(client_id, song_id, order):
            retval = 'Success'
        else:
            retval = 'Failed'
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

    def singer_song_fetch(self, song_id):
        return json.dumps(self.db.singer_song_fetch(song_id))

if __name__ == '__main__':
    s = stv_server('root', 'root', 'stv_db')
    s.recommendation_fetch('1')
    # s.top_fetch('random')
    # s.top_fetch('comment')
