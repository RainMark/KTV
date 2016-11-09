#!/usr/python3

import mysql.connector as mariadb

class stv_trigger(object):
    def __init__(self):
        pass

    def csong_update_after_delete(self, db, client_id, old_order):
        sql = 'Update C_Song Set C_Order = C_Order - 1 Where C_Order > %d' % (old_order)
        print(old_order)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            return True
        except:
            db.rollback()
            return False

    def csong_update_before_insert(self, db, client_id, limit_order):
        sql = 'Update C_Song Set C_Order = C_Order + 1 Where C_Order >= %d' % (limit_order)
        print(limit_order)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
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

    def close(self):
        self.database.close()

    def hot_all(self):
        'Return the most hot MVs as click rate.'
        query = 'Select * From Song Order By songmonth DESC'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        # for item in data[0:10]:
        #     print(item)
        return data[0:10]

    def hot_zh(self):
        'Return the most hot Chinese MVs as click rate.'
        query = 'Select * From Song Where songlanguage=\'中文\' Order By songmonth DESC'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        # for item in data[0:10]:
        #     print(item)
        return data[0:10]

    def hot_not_zh(self):
        'Return the most hot MVs as click rate.'
        query = 'Select * From Song Where songlanguage!=\'中文\' Order By songmonth DESC'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        # for item in data[0:10]:
        #     print(item)
        return data[0:10]

    def playing_list_fetch(self, client_id):
        sql = 'Select Song.SongID, Song.SongName From Song, C_Song Where Song.SongID = C_Song.SongID && ClientID = %s Order By C_Order' % (client_id)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            # for item in data:
            #     print(item)
            return data
        except:
            return [()]

    def playing_list_add(self, client_id, song_id):
        sql = 'Select count(C_Order) From C_Song Where ClientID = %s' % (client_id)
        try:
            self.cursor.execute(sql)
            order = int(self.cursor.fetchall()[0][0])
        except:
            return False

        # print(order)
        sql = 'Insert into C_Song(SongID, ClientID, C_Order) Value(%s, %s, %d)' % (song_id, client_id, order + 1)
        try:
            self.cursor.execute(sql)
            self.database.commit()
            return True

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return False

    def playing_list_delete(self, client_id, song_id):
        sql = 'Select C_Order From C_Song Where ClientID = %s && SongID = %s' % (client_id, song_id)
        try:
            self.cursor.execute(sql)
            order = int(self.cursor.fetchall()[0][0])
        except:
            print('Execute SQL Except: ', sql)
            return False

        sql = 'Delete From C_Song Where ClientID = %s && SongID = %s' % (client_id, song_id)
        try:
            self.cursor.execute(sql)
            # self.database.commit()
            return self.trigger.csong_update_after_delete(self.database, client_id, order)

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

        sql = 'Insert into C_Song(SongID, ClientID, C_Order) Value(%s, %s, %d)' % (song_id, client_id, order)
        try:
            self.cursor.execute(sql)
            self.database.commit()
            return True

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return False

    def search_singer_by_abridge(self, key):
        sql = "Select StarID, StarName, StarRegion, StarStyle From Star Where StarNameAbridge Like \'%s\'"
        print(key)
        try:
            self.cursor.execute(sql, (key + r'%'))
            # return self.cursor.fetchall()
            data = self.cursor.fetchall()
            for v in data:
                print(v)
            return data

        except:
            self.database.rollback()
            print('Execute SQL Except: ', sql)
            return (())


if __name__ == '__main__':
    run = stv_mariadb('root', 'root', 'ktv_db')
    # run.hot_all()
    # run.playing_list_fetch(1)
    # run.playing_list_add(3, 51)
    # run.playing_list_add(3, 52)
    # run.playing_list_add(3, 53)
    # run.playing_list_add(3, 54)
    # run.playing_list_add(3, 55)
    # run.playing_list_delete(3, 54)
    # run.playing_list_resort(3, 53, 4)
    run.search_singer_by_abridge('L')
    run.close()
