#!/usr/python3

from urllib import request
import json

MACHINE_ID = 2
# global MACHINE_ID

class stv_request_class(object):
    def __init__(self):
        pass

    def list_fetch(self, client_id = MACHINE_ID):
        url = 'http://127.0.0.1:5000/playing/fetch/%d' % (client_id)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))
            # data = f.read()
            # print('Status:', f.status, f.reason)
            # for k, v in f.getheaders():
            #     print('%s: %s' % (k, v))
            # print('Data:', data.decode('utf-8'))
            # print('List:', json.loads(data.decode('utf-8')))

    def list_add(self, song_id, client_id = MACHINE_ID):
        pass

    def list_delete(self, song_id, client_id = MACHINE_ID):
        pass

    def top_fetch(self, top_type = 'all'):
        pass

if __name__ == '__main__':
    req = stv_request_class()
    for song in req.list_fetch():
        print(song)
