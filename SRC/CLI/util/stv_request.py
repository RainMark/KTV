#!/usr/python3

from urllib import request
import shutil
import json
import os

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

    def play_list_move(self, song_id):
        url = self.uri + '/playing/resort/%s/%s/1' % (self.machine, song_id)
        print(url)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    def play_list_add(self, song_id):
        url = self.uri + '/playing/add/%s/%s' % (self.machine, song_id)
        print(url)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    def play_list_remove(self, song_id):
        url = self.uri + '/playing/delete/%s/%s' % (self.machine, song_id)
        print(url)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    def top_fetch(self, top_type = 'all'):
        url = self.uri + '/top/%s' % (top_type)
        print(url)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    def download(self, song_id, directory = '/tmp/stv'):
        retval = os.path.isdir(directory)
        if not retval:
            os.mkdir(directory)

        url = self.uri + '/download/%s' % (song_id)
        # print(url)
        path = os.path.join(directory, song_id)
        # print(path)
        with request.urlopen(url) as f:
            header = dict(f.getheaders())
            length = int(header['Content-Length'])
            if 4 == length:
                return None

            with open(path, 'wb') as out_file:
                shutil.copyfileobj(f, out_file)

        return path


if __name__ == '__main__':
    req = stv_request_class('http://localhost:5000', '2')
    # for song in req.play_list_fetch():
    #     print(song)
    req.download('4')
