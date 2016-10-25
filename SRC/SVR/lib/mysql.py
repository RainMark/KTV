#!/usr/python3

# import mysql.connector as mariadb

class mdb:
    def __init__(self):
        self.database = mariadb.connect(user='root', password='root', database='ktv_db')
        self.cursor = self.database.cursor()

    def close(self):
        self.database.close()

    def hot100(self):
        'Return the most hot 100 MV as year rate.'
