#!/usr/python3

from urllib import request, error, parse
import shutil, json, os

def network_check(func):
    def wrapper(*args, **kw):
        req = args[0]
        try:
            retval = func(*args, **kw)
            req.online = True
            return retval
        except error.HTTPError as e1:
            print(e1)
            req.online = False
        except error.URLError as e2:
            print(e2)
            req.online = False
    return wrapper

class stv_request_class(object):
    def __init__(self, uri, machine):
        self.uri = uri
        self.machine = machine
        self.online = False

    @network_check
    def sequence_init(self, seq):
        url = self.uri + '/desktop/insert/%s/%s' % (self.machine, seq)
        print(url)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def play_list_fetch(self):
        url = self.uri + '/playing/fetch/' + self.machine
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def his_list_fetch(self):
        url = self.uri + '/history/fetch/' + self.machine
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def play_list_move(self, song_id):
        url = self.uri + '/playing/resort/%s/%s/2' % (self.machine, song_id)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def play_list_add(self, song_id):
        url = self.uri + '/playing/add/%s/%s' % (self.machine, song_id)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def play_list_remove(self, song_id):
        url = self.uri + '/playing/delete/%s/%s' % (self.machine, song_id)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def top_fetch(self, top_type = 'all'):
        url = self.uri + '/top/%s' % (top_type)
        print(url)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def comment_fetch(self, song_id):
        url = self.uri + '/comment/fetch/%s' % (song_id)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def search_singer_by_fullname(self, key):
        key = parse.quote(key.encode('utf-8')) # Solved Unicode URL
        url = self.uri + '/search/fullname/singer/%s' % (key)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def search_singer_by_abridge(self, key):
        key = parse.quote(key.encode('utf-8'))
        url = self.uri + '/search/abbreviation/singer/%s' % (key)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def search_song_by_fullname(self, key):
        key = parse.quote(key.encode('utf-8'))
        url = self.uri + '/search/fullname/song/%s' % (key)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def search_song_by_abridge(self, key):
        key = parse.quote(key.encode('utf-8'))
        url = self.uri + '/search/abbreviation/song/%s' % (key)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def singer_song_fetch(self, singer_id):
        url = self.uri + '/singer/fetch/%s' % (singer_id)
        with request.urlopen(url) as f:
            return json.loads(f.read().decode('utf-8'))

    @network_check
    def download(self, song_id, directory = '/tmp/stv/mv'):
        retval = os.path.isdir(directory)
        if not retval:
            os.mkdir(directory)

        url = self.uri + '/download/mv/%s' % (song_id)
        path = os.path.join(directory, song_id)
        with request.urlopen(url) as f:
            header = dict(f.getheaders())
            length = int(header['Content-Length'])
            if 4 == length:
                return None

            with open(path, 'wb') as out_file:
                shutil.copyfileobj(f, out_file)

        return path

    @network_check
    def album_fetch(self, star_id, directory = '/tmp/stv/album'):
        retval = os.path.isdir(directory)
        if not retval:
            os.mkdir(directory)

        url = self.uri + '/download/album/%s' % (star_id)
        path = os.path.join(directory, star_id)
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
    req.album_fetch('2')
