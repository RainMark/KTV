#!/usr/python3


import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

sys.path.append(os.path.join(os.getcwd(), 'util'))
from stv_request import stv_request_class as stv_req

class stv_signal_handler(object):
    def stv_exit(self, *args):
        Gtk.main_quit(*args)


class stv_class(object):
    def __init__(self):
        self.UI_bind()
        self.SVR_bind()
        pass

    def UI_bind(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/main.xml")
        self.window = self.builder.get_object("window")
        self.builder.connect_signals(stv_signal_handler())
        self.window.show_all()

    def SVR_bind(self):
        self.req = stv_req()


if __name__ == '__main__':
    app = stv_class()
    Gtk.main()
