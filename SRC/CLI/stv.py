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


class stv_popmenu(object):
    def __init__(self, menu):
        self.menu = menu

    def show_all(self, widget, event):
        # if event.type == Gtk.BUTTON_PRESS and event.button == 3:
        if event.button == 3:
            print("show")
            # print(dir(self.menu))
            # pos = self.menu.get_position()
            # print(pos.LEFT, pos.RIGHT)
            # self.menu.show_all()
            self.menu.set_relative_to(widget)
            # self.menu.popup(None, None, None, None, 0, Gtk.get_current_event_time())
            self.menu.popup()

    def hide(self):
        self.menu.hide()

    def connect_signal(self, obj, signal):
        obj.connect(signal, self.show_all)



class stv_class(object):
    def __init__(self):
        self.UI_build()
        self.SVR_init()

    def UI_build(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/main.xml")
        self.window = self.builder.get_object("window")

        self.rightclick = stv_popmenu(self.builder.get_object("rightclick"))
        self.rightclick.connect_signal(self.builder.get_object("tv_playing"), "button-press-event")

        self.builder.connect_signals(stv_signal_handler())
        # self.UI_apply_css()
        self.window.show_all()

    def UI_apply_css(self):
        self.style_provider = Gtk.CssProvider()
        self.style_provider.load_from_path('glade/main.css')
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def SVR_init(self):
        self.req = stv_req()


if __name__ == '__main__':

    def UI_build(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/main.xml")
        self.window = self.builder.get_object("window")
        self.rightclick = self.builder.get_object("rightclick")
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
