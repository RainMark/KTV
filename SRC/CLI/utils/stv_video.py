#!/usr/bin/python3

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gst, Gtk
from gi.repository import GdkX11, GstVideo
from os import path

class stv_video_player_class(object):
    def __init__(self, obj, obj_hook):
        GObject.threads_init()
        Gst.init(None)
        self.obj = obj
        self.obj_hook = obj_hook
        self.state = Gst.State.NULL
        self.pipeline = Gst.Pipeline()

    def pause(self):
            self.pipeline.set_state(Gst.State.PAUSED)
            self.state = Gst.State.PAUSED

    def play(self):
        if Gst.State.PLAYING == self.state:
            return None
        else:
            self.pipeline.set_state(Gst.State.PLAYING)
            self.state = Gst.State.PLAYING

    def ready(self, filepath):
        self.pipeline.set_state(Gst.State.NULL)
        self.pipeline = Gst.Pipeline()
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message::eos', self.on_eos)
        self.bus.connect('message::error', self.on_error)
        self.bus.enable_sync_message_emission()
        self.bus.connect('sync-message::element', self.on_sync_message)
        self.playbin = Gst.ElementFactory.make('playbin', None)
        self.pipeline.add(self.playbin)
        self.uri = filepath
        self.playbin.set_property('uri', self.uri)
        self.pipeline.set_state(Gst.State.NULL)
        self.state = Gst.State.PAUSED

    def set_xid(self, area):
        '''
        # self.window.show_all()
        # You need to get the XID after window.show_all().  You shouldn't get it
        # in the on_sync_message() handler because threading issues will cause
        # segfaults there.
        # self.xid = self.disp_area.get_property('window').get_xid()
        '''
        self.xid = area.get_window().get_xid()

    def stop(self):
        self.pipeline.set_state(Gst.State.NULL)
        self.ready('file://' + path.abspath('resources/blank.mp4'))
        self.play()
        self.pause()
        self.state = Gst.State.NULL

    def exit(self):
            self.pipeline.set_state(Gst.State.NULL)

    def on_sync_message(self, bus, msg):
        if msg.get_structure().get_name() == 'prepare-window-handle':
            msg.src.set_window_handle(self.xid)

    def on_eos(self, bus, msg):
        self.obj_hook(self.obj)

    def on_error(self, bus, msg):
        self.obj_hook(self.obj)

if __name__ == '__main__':
    pass
