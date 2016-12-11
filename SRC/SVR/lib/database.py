#!/usr/python3

import mysql.connector as mariadb

class stv_trigger(object):
    def __init__(self):
        pass

    def csong_update_after_delete(self, db, client_id, old_order):
        sql = 'Update C_Song Set S_Order = S_Order - 1 Where S_Order > %s'
        print(old_order)
        cursor = db.cursor()
        try:
            cursor.execute(sql, [old_order])
            db.commit()
            return True
        except:
            db.rollback()
            return False

    def csong_update_before_insert(self, db, client_id, limit_order):
        sql = 'Update C_Song Set S_Order = S_Order + 1 Where S_Order >= %s'
        print(limit_order)
        cursor = db.cursor()
        try:
            cursor.execute(sql, [limit_order])
            # db.commit()
            return True
        except:
            db.rollback()
            return False


class stv_mariadb(object):
    def __init__(self, muser, mpassword, mdatabase):
        self.database = mariadb.connect(user=muser, password=mpassword, database=mdatabase)
        self.cursor = self.database.cursor()
        self.trigger = stv_trigger()
        self.hot_map_sql = {
            'hotall'    :' From Song, Star Where Song.StarID = Star.StarID Order By SongYear DESC',
            'hotzh'     :' From Song, Star Where Song.StarID = Star.StarID And SongLanguage = \'中文\' Order By SongYear DESC',
            'hoten'     :' From Song, Star Where Song.StarID = Star.StarID And SongLanguage = \'英文\' Order By SongYear DESC',
            'hotweek'   :' From Song, Star Where Song.StarID = Star.StarID Order By SongWeek DESC',
            'hotmonth'  :' From Song, Star Where Song.StarID = Star.StarID Order By SongMonth DESC',
            'hotnew'    :' From Song, Star Where Song.StarID = Star.StarID Order By SongDate DESC'
        }

    def close(self):
        self.database.close()

    def hot_fetch(self, hot_type):
        if None == self.hot_map_sql.get(hot_type):
            return []

        sql = 'Select SongID, SongName, StarName, SongType, SongLanguage' + self.hot_map_sql[hot_type]
        print(sql)

        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for item in data[0:50]:
            print(item)
        return data[0:50]

    def comment_fetch(self, song_id):
        sql = 'Select C_Content From Comment Where SongID = %s'
        try:
            data = []
            self.cursor.execute(sql, [song_id])
            raw = self.cursor.fetchall()
            for v in raw[0:20]:
                data.append(v[0])
            return data
        except:
            return []

    def playing_list_fetch(self, client_id):
        sql = 'Select Song.SongID, Song.SongName From Song, C_Song Where Song.SongID = C_Song.SongID && ClientID = %s Order By S_Order'
        try:
            self.cursor.execute(sql, [client_id])
            data = self.cursor.fetchall()
            for item in data:
                print(item)
            return data
        except:
            return []

    def playing_list_add(self, client_id, song_id):
        sql = 'Select count(S_Order) From C_Song Where ClientID = %s'
        try:
            self.cursor.execute(sql, [client_id])
            order = int(self.cursor.fetchall()[0][0])
        except:
            return False

        # print(order)
        sql = 'Insert into C_Song(SongID, ClientID, S_Order) Value(%s, %s, %s)'
        try:
            self.cursor.execute(sql, [song_id, client_id, order + 1])
            self.database.commit()
            return True

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return False

    def playing_list_delete(self, client_id, song_id):
        sql = 'Select S_Order From C_Song Where ClientID = %s && SongID = %s'
        try:
            self.cursor.execute(sql, [client_id, song_id])
            order = int(self.cursor.fetchall()[0][0])
        except:
            print('Execute SQL Except: ', sql)
            return False

        sql = 'Delete From C_Song Where ClientID = %s && SongID = %s'
        try:
            self.cursor.execute(sql, [client_id, song_id])
            # self.database.commit()
            ret = self.trigger.csong_update_after_delete(self.database, client_id, order)
            if ret:
                self.history_list_insert(client_id, song_id)
                return True
            else:
                return False

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return False

    def playing_list_resort(self, client_id, song_id, order):
        if True != self.playing_list_delete(client_id, song_id):
            return False

        retval = self.trigger.csong_update_before_insert(self.database, client_id, order)
        if True != retval:
            return retval

        sql = 'Insert into C_Song(SongID, ClientID, S_Order) Value(%s, %s, %s)'
        try:
            self.cursor.execute(sql, [song_id, client_id, order])
            self.database.commit()
            return True

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return False

    def history_list_fetch(self, client_id):
        sql = 'Select Song.SongID, Song.SongName From Song, History Where Song.SongID = History.SongID && ClientID = %s'
        try:
            self.cursor.execute(sql, [client_id])
            data = self.cursor.fetchall()
            for item in data:
                print(item)
            return data
        except:
            return []

    def history_list_insert(self, client_id, song_id):
        sql = 'Insert into History(SongID, ClientID) Value(%s, %s)'
        try:
            self.cursor.execute(sql, [song_id, client_id])
            self.database.commit()
            return True

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return False

    def search_singer_by_abridge(self, key):
        sql = 'Select StarID, StarName, StarRegion, StarStyle From Star Where StarNameAbridge Like %s'
        try:
            self.cursor.execute(sql, [key + r'%'])
            # return self.cursor.fetchall()
            data = self.cursor.fetchall()
            for v in data:
                print(v)
            return data

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return []

    def search_singer_by_fullname(self, key):
        sql = 'Select StarID, StarName, StarRegion, StarStyle From Star Where StarName Like %s'
        try:
            self.cursor.execute(sql, [key + r'%'])
            # return self.cursor.fetchall()
            data = self.cursor.fetchall()
            for v in data:
                print(v)
            return data

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return []

    def search_song_by_fullname(self, key):
        'SongID | SongName | SongType | SongLanguage | SongNameAbridge | StarID'
        sql = 'Select SongID, SongName, StarName, SongType, SongLanguage From Song, Star Where Star.StarID = Song.StarId And SongName Like %s'
        try:
            self.cursor.execute(sql, [key + r'%'])
            # return self.cursor.fetchall()
            data = self.cursor.fetchall()
            for v in data:
                print(v)
            return data

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return []

    def search_song_by_abridge(self, key):
        'SongID | SongName | SongType | SongLanguage | SongNameAbridge | StarID'
        sql = 'Select SongID, SongName, StarName, SongType, SongLanguage From Song, Star Where Star.StarID = Song.StarID And SongNameAbridge Like %s'
        try:
            self.cursor.execute(sql, [key + r'%'])
            # return self.cursor.fetchall()
            data = self.cursor.fetchall()
            for v in data:
                print(v)
            return data

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return []

    def singer_song_fetch(self, singer_id):
        sql = 'Select SongID, SongName, StarName, SongType, SongLanguage From Song, Star Where Song.StarID = %s And Star.StarID = Song.StarID'
        try:
            self.cursor.execute(sql, [singer_id])
            # return self.cursor.fetchall()
            data = self.cursor.fetchall()
            for v in data:
                print(v)
            return data

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return []

    def user_get_all(self):
        sql = 'Select ClientID, SongID From History'
        try:
            self.cursor.execute(sql)
            # return self.cursor.fetchall()
            data = self.cursor.fetchall()
            # for v in data:
            #     print(v)
            return data

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return []

if __name__ == '__main__':
    run = stv_mariadb('root', 'root', 'stv_db')
    # run.hot_zh()
    # run.hot_all()
    # print('')
    # run.playing_list_fetch(3)
    # print('')
    # run.playing_list_add(3, 51)
    # print('')
    # run.playing_list_add(3, 52)
    # run.playing_list_add(3, 53)
    # run.playing_list_add(3, 54)
    # run.playing_list_add(3, 55)
    # print('')
    # run.playing_list_delete(3, 54)
    # run.playing_list_resort(3, 53, 4)
    # print('')
    # run.search_singer_by_abridge('Lj')
    # print('')
    # run.search_singer_by_fullname('周')
    # print('')
    # run.search_song_by_abridge('X')
    # print('')
    # run.search_song_by_fullname('喜')
    # run.user_get_all()
    # run.history_list_fetch('1')
    # run.history_list_insert('1', '22')
    # run.history_list_fetch('1')
    # run.comment_fetch('2')
    run.singer_song_fetch('115')
    run.close()
