#!/usr/bin/python3

import json, os, logging
from urllib import request

class yyt_api_class(object):
    def __init__(self):
        self.yyt_uri = 'http://ext.yinyuetai.com/main/get-h-mv-info?json=true&videoId='

    def open_url(self, url):
        try:
            with request.urlopen(url) as f:
                return json.loads(f.read().decode('utf-8'))
        except:
            return None

    def analyze_music_video_id(self, id):
        obj = self.open_url(self.yyt_uri + id)
        if None == obj or None == obj.get('videoInfo'):
            return 'resources/blank.mp4'

        videoUrlModels = obj['videoInfo']['coreVideoInfo']['videoUrlModels']
        if 0 == videoUrlModels.__len__():
            return 'resources/blank.mp4'
        else:
            videoUrl = videoUrlModels[-1]['videoUrl']
            return videoUrl

if __name__ == '__main__':
    yyt = yyt_api_class()
    Url = yyt.analyze_music_video_id('15444')
    print(Url)

