#!/usr/python3


import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

sys.path.append(os.path.join(os.getcwd(), 'util'))
from stv_request import stv_request_class as stv_req

class stv_signal_handler(object):
    def stv_exit(self, *args):
        Gtk.main_quit(*args)


class stv_class(object):
    def __init__(self):
        self.UI_build()
        self.SVR_init()

    def UI_build(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/main.xml")
        self.window = self.builder.get_object("window")
        self.builder.connect_signals(stv_signal_handler())
        #self.UI_apply_css()
        self.window.show_all()

    def UI_apply_css(self):
        self.style_provider = Gtk.CssProvider()
        self.style_provider.load_from_path('glade/main.css')
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def SVR_init(self):
        self.req = stv_req()


if __name__ == '__main__':
    app = stv_class()
    Gtk.main()
