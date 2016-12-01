#!/usr/bin/python3

from os import path
import time

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gst, Gtk
# Needed for window.get_xid(), xvimagesink.set_window_handle(), respectively:
from gi.repository import GdkX11, GstVideo




class stv_video_player_class(object):
    def __init__(self, area):
        GObject.threads_init()
        Gst.init(None)
        # self.window = Gtk.Window()
        # self.window.connect('destroy', self.quit)
        # self.window.set_default_size(800, 450)

        # self.drawingarea = Gtk.DrawingArea()
        self.disp_area = area
        # self.window.add(self.drawingarea)

        # Create GStreamer pipeline
        self.pipeline = Gst.Pipeline()

        # Create bus to get events from GStreamer pipeline
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message::eos', self.on_eos)
        self.bus.connect('message::error', self.on_error)

        # This is needed to make the video output in our DrawingArea:
        self.bus.enable_sync_message_emission()
        self.bus.connect('sync-message::element', self.on_sync_message)

        # Create GStreamer elements
        self.playbin = Gst.ElementFactory.make('playbin', None)

        # Add playbin to the pipeline
        self.pipeline.add(self.playbin)

        # Set properties

    def change_area(self, area):
        self.pipeline.set_state(Gst.State.PAUSED)
        self.bus.remove_watch()
        self.bus.disable_sync_message_emission()
        self.xid = area.get_window().get_xid()
        # self.bus.enable_sync_message_emission()
        self.cur_pos = self.pipeline.query_position(Gst.Format.TIME)[1]
        # self.pipeline.set_state(Gst.State.NULL)
        print('Pause: ', self.cur_pos)
        # seek_ns = self.cur_pos - 10 * 1000000000
        # if seek_ns < 0:
        #     seek_ns = 0
        # print('Seek_ns: ', seek_ns)
        # self.pipeline.set_state(Gst.State.READY)
        # self.pipeline.seek_simple(Gst.Format.TIME, Gst.SeekFlags.SNAP_BEFORE, seek_ns)
        # time.sleep(1)
        print('Sleep OK')
        self.pipeline.set_state(Gst.State.PLAYING)
        self.pipeline.seek_simple(Gst.Format.TIME, Gst.SeekFlags.SNAP_BEFORE, self.cur_pos)
        self.pipeline.set_state(Gst.State.PAUSED)
        self.cur_pos = self.pipeline.query_position(Gst.Format.TIME)[1]
        print('Seeked: ', self.cur_pos)
        # self.pipeline.set_state(Gst.State.READY)
        # self.pipeline.seek_simple(Gst.Format.TIME, Gst.SeekFlags.SNAP_BEFORE, self.cur_pos)
        # self.cur_pos = self.pipeline.query_position(Gst.Format.TIME)[1]
        # print(self.cur_pos)
        # print(self.xid)

    def ready(self, filename):
        self.file= path.join(path.dirname(path.abspath(__file__)), filename)
        self.uri = 'file://' + self.file
        self.playbin.set_property('uri', self.uri)
        self.pipeline.set_state(Gst.State.NULL)

    def run(self):
        # self.window.show_all()
        # You need to get the XID after window.show_all().  You shouldn't get it
        # in the on_sync_message() handler because threading issues will cause
        # segfaults there.
        # time.sleep(0.1)
        srt, st, stp = self.pipeline.get_state(Gst.CLOCK_TIME_NONE)
        if Gst.State.PLAYING == st:
            return None
        # self.xid = self.disp_area.get_property('window').get_xid()
        self.xid = self.disp_area.get_window().get_xid()
        print(self.xid)
        self.pipeline.set_state(Gst.State.PLAYING)
        # self.pipeline.set_state(Gst.State.PAUSED)
        # Gtk.main()

    def quit(self):
        self.pipeline.set_state(Gst.State.NULL)
        # Gtk.main_quit()

    def on_sync_message(self, bus, msg):
        if msg.get_structure().get_name() == 'prepare-window-handle':
            print('prepare-window-handle')
            msg.src.set_window_handle(self.xid)

    def on_eos(self, bus, msg):
        print('on_eos(): seeking to start of video')
        self.pipeline.seek_simple(
            Gst.Format.TIME,
            Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT,
            0
        )

    def on_error(self, bus, msg):
        print('on_error():', msg.parse_error())


if __name__ == '__main__':
    pass
