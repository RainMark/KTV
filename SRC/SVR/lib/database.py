#!/usr/python3

import mysql.connector as mariadb

class mdb(object):
    def __init__(self, muser, mpassword, mdatabase):
        self.database = mariadb.connect(user=muser, password=mpassword, database=mdatabase)
        self.cursor = self.database.cursor()

    def close(self):
        self.database.close()

    def hot_all(self):
        'Return the most hot MVs as click rate.'
        query = 'Select * From Song Order By songmonth DESC'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        for item in data[0:10]:
            print(item)
        return data[0:10]

    def hot_zh(self):
        'Return the most hot Chinese MVs as click rate.'
        query = 'Select * From Song Where songlanguage=\'中文\' Order By songmonth DESC'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        for item in data[0:10]:
            print(item)
        return data[0:10]

    def hot_not_zh(self):
        'Return the most hot MVs as click rate.'
        query = 'Select * From Song Where songlanguage!=\'中文\' Order By songmonth DESC'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        for item in data[0:10]:
            print(item)
        return data[0:10]


if __name__ == '__main__':
    run = mdb('root', 'root', 'ktv_db')
    run.hot_all()
    run.close()
