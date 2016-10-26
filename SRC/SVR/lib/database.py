#!/usr/python3

import mysql.connector as mariadb

class mdb(object):
    def __init__(self, muser, mpassword, mdatabase):
        self.database = mariadb.connect(user=muser, password=mpassword, database=mdatabase)
        self.cursor = self.database.cursor()

    def close(self):
        self.database.close()

    def hot100(self):
        'Return the most hot 100 MV as year rate.'
        query = 'Select * From Song Order By songmonth DESC'
        self.cursor.execute(query)
        data = self.cursor.fetchmany(200)
        print(len(data))
        for item in data:
            print(item)

if __name__ == '__main__':
    run = mdb('root', 'root', 'ktv_db')
    run.hot100()
    run.close()

