#!/usr/python3

import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

sys.path.append(os.path.join(os.getcwd(), 'util'))
from stv_request import stv_request_class as stv_req

global app

class stv_signal_handler(object):
    def stv_exit(self, *args):
        Gtk.main_quit(*args)

    def stv_hotall(self, widget):
        self.stv_back()
        box = app.builder.get_object("box_rank")
        child = box.get_children()
        box.remove(child[0])
        box.add(app.builder.get_object("show_list"))
        app.stack_box = box
        app.stack_box_child = child[0]
        app.restored = False

    def stv_guess(self, widget):
        self.stv_back()
        box = app.builder.get_object("box_recommend")
        child = box.get_children()
        box.remove(child[0])
        box.add(app.builder.get_object("show_list"))
        app.stack_box = box
        app.stack_box_child = child[0]
        app.restored = False

    def stv_back(self, *args):
        if app.restored:
            return None

        app.stack_box.remove(app.stack_box.get_children()[0])
        app.stack_box.add(app.stack_box_child)
        app.restored = True



class stv_popmenu(object):
    def __init__(self, menu):
        self.menu = menu

    def show_all(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
            self.menu.set_relative_to(widget)
            pos = Gdk.Rectangle()
            pos.x = event.x + 25
            pos.y = event.y + 25
            pos.width = 0
            pos.height = 0
            self.menu.set_pointing_to(pos)
            self.menu.popup()

    def hide(self):
        self.menu.hide()

    def connect_signal(self, obj, signal):
        obj.connect(signal, self.show_all)



class stv_class(object):
    def __init__(self):
        self.UI_build()
        self.SVR_init()
        self.restored = True

    def UI_build(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/main.xml")
        self.window = self.builder.get_object("window")

        self.rightclick = stv_popmenu(self.builder.get_object("rightclick"))
        self.rightclick.connect_signal(self.builder.get_object("tv_playing"), "button-press-event")

        self.show_list = self.builder.get_object("lt_result")

        self.builder.connect_signals(stv_signal_handler())
        self.UI_apply_css()
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
