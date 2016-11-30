#!/usr/python3

from urllib import request
import json

class stv_request_class(object):
    def __init__(self, uri, machine):
        self.uri = uri
        self.machine = machine
        pass

    def play_list_fetch(self):
        url = self.uri + '/playing/fetch/' + self.machine
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))
            # data = f.read()
            # print('Status:', f.status, f.reason)
            # for k, v in f.getheaders():
            #     print('%s: %s' % (k, v))
            # print('Data:', data.decode('utf-8'))
            # print('List:', json.loads(data.decode('utf-8')))

    def play_list_move(self, sid):
        url = self.uri + '/playing/resort/%s/%s/1' % (self.machine, sid)
        print(url)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    def play_list_add(self, song_id):
        pass

    def play_list_remove(self, song_id):
        pass

    def top_fetch(self, top_type = 'all'):
        pass

if __name__ == '__main__':
    req = stv_request_class('http://localhost:5000', '2')
    for song in req.play_list_fetch():
        print(song)
