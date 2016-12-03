#!/usr/python3

import os, signal
import time
import sys
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gst', '1.0')
from gi.repository import Gtk, Gdk, GObject, Gst

sys.path.append(os.path.join(os.getcwd(), 'util'))
from stv_request import stv_request_class
from stv_video import stv_video_player_class

global app

class stv_signal_handler(object):
    def stv_exit(self, *args):
        app.player.stop()
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
        app.req_type = 'topall'
        app.result_list_refresh()

    def stv_guess(self, widget):
        self.stv_back()
        box = app.builder.get_object("box_recommend")
        child = box.get_children()
        box.remove(child[0])
        box.add(app.builder.get_object("show_list"))
        app.stack_box = box
        app.stack_box_child = child[0]
        app.restored = False
        app.req_type = 'guess'
        app.result_list_refresh()

    def stv_back(self, *args):
        if app.restored:
            return None

        app.stack_box.remove(app.stack_box.get_children()[0])
        app.stack_box.add(app.stack_box_child)
        app.restored = True

    def stv_play_refresh(self, *args):
        app.play_menu.hide()
        app.play_list_update()

    def stv_play_remove(self, *args):
        app.play_menu.hide()
        app.play_list_remove()

    def stv_play_move(self, *args):
        app.play_menu.hide()
        app.play_list_move()

    def stv_result_refresh(self, *args):
        app.res_menu.hide()
        app.result_list_refresh()

    def stv_result_add(self, *args):
        app.res_menu.hide()
        app.result_list_add()

    def stv_mv_show(self, *args):
        if app.in_mv:
            return None

        app.box_disp.set_vexpand(True)
        app.box_disp.set_hexpand(True)
        app.box_disp.set_valign(Gtk.Align.FILL)
        app.box_disp.set_halign(Gtk.Align.FILL)
        app.box_disp.set_margin_top(5)
        app.box_disp.set_margin_bottom(10)
        app.box_disp.set_margin_left(10)
        app.box_disp.set_margin_right(10)

        app.box_main.remove(app.box_menu)
        gd = app.grid_mv
        gd.remove_column(1)
        gd.insert_row(0)
        gd.attach(app.bt_mv_back, 0, 0, 1, 1)
        gd.attach(app.box_phrase, 0, 2, 1, 1)
        gd.attach(app.box_ctrl,   0, 3, 1, 1)
        gd.attach(app.sc_comment, 1, 0, 1, 3)

        # app.window.set_size_request(1022, 500)
        app.in_mv = True

    def stv_mv_hide(self, *args):
        app.box_disp.set_vexpand(False)
        app.box_disp.set_hexpand(False)
        app.box_disp.set_valign(Gtk.Align.CENTER)
        app.box_disp.set_halign(Gtk.Align.CENTER)
        app.box_disp.set_margin_top(0)
        app.box_disp.set_margin_bottom(0)
        app.box_disp.set_margin_left(0)
        app.box_disp.set_margin_right(0)

        gd = app.grid_mv
        gd.remove_column(1)
        gd.remove_row(3)
        gd.remove_row(2)
        gd.remove_row(0)
        gd.attach(app.box_ctrl, 1, 0, 1, 1)

        app.box_main.add(app.box_menu)
        # app.window.set_size_request(1022, 500)
        app.in_mv = False

    def stv_mv_play(self, *args):
        if Gst.State.PLAYING == app.player.state:
            app.player.pause()
            app.bt_play.set_image(app.pause_img)
        else:
            app.player.play()
            app.bt_play.set_image(app.play_img)

    def stv_mv_next(self, *args):
        pass


class stv_popover(object):
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
            self.x = event.x
            self.y = event.y
            self.menu.set_pointing_to(pos)
            self.menu.popup()

    def hide(self):
        self.menu.hide()

    def connect_signal(self, obj, signal):
        obj.connect(signal, self.show_all)


class stv_class(object):
    def __init__(self, server, machine):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.UI_build()
        self.check_network(server, machine)
        self.play_list_update()

        self.restored = True
        self.req_type = 'topall'
        self.last_operation = None
        self.in_mv = False

    def check_network(self, svr, mach):
        self.SVR_init(svr, mach)

    def UI_build(self):
        self.builder           = Gtk.Builder()
        self.builder.add_from_file("glade/main.xml")

        self.play_menu         = stv_popover(self.builder.get_object("play_menu"))
        self.res_menu          = stv_popover(self.builder.get_object("res_menu"))
        self.window            = self.builder.get_object("window")
        self.box_main          = self.builder.get_object('box_main')
        self.box_menu          = self.builder.get_object('box_menu')
        self.play_list_store   = self.builder.get_object("lt_playing")
        self.play_view         = self.builder.get_object("tv_playing")
        self.res_list_store    = self.builder.get_object("lt_result")
        self.res_view          = self.builder.get_object("tv_result")
        self.disp_area         = self.builder.get_object('disp_area')
        self.box_disp          = self.builder.get_object('box_disp')
        self.grid_mv           = self.builder.get_object('grid_mv')
        self.box_phrase        = self.builder.get_object('phrase')
        self.bt_mv_back        = self.builder.get_object('bt_mv_back')
        self.bt_play           = self.builder.get_object('bt_play')
        self.sc_comment        = self.builder.get_object('comment')
        self.box_ctrl          = self.builder.get_object('box_ctrl')
        self.play_img          = self.builder.get_object('bt_play_img')
        self.pause_img         = self.builder.get_object('bt_pause_img')
        self.player            = stv_video_player_class()

        # Setup control buttons
        self.box_disp.set_valign(Gtk.Align.END)
        self.box_disp.set_halign(Gtk.Align.START)
        self.grid_mv.attach(self.box_ctrl, 1, 0, 1, 1)

        # Setup right click popover menu
        self.play_menu.connect_signal(self.play_view, "button-press-event")
        self.res_menu.connect_signal(self.res_view, "button-press-event")
        self.builder.connect_signals(stv_signal_handler())

        self.UI_apply_css()
        self.window.show_all()

        # In self.player, get_xid() can be called after window.show_all()
        self.player.set_xid(self.disp_area)
        self.player.ready('Red.mp4')

    def UI_apply_css(self):
        self.style_provider = Gtk.CssProvider()
        self.style_provider.load_from_path('glade/main.css')
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def SVR_init(self, svr, mach):
        self.req = stv_request_class(svr, mach)

    def play_list_update(self):
        data = self.req.play_list_fetch()
        store = self.play_list_store
        if None != data:
            store.clear()
        for idx, meta in enumerate(data):
            store.append([idx, meta[1], meta[0]])

    def play_list_move(self):
        path, column = self.play_view.get_cursor()
        if None == path:
            return None

        store = self.play_list_store
        it = store.get_iter(path)
        print("Selected row: ", store[it][0:])
        sid = store[it][2]
        retval = self.req.play_list_move(sid)
        print(retval)
        if 'Resort OK' == retval:
            self.play_list_update()

    def play_list_remove(self):
        path, column = self.play_view.get_cursor()
        if None == path:
            return None

        store = self.play_list_store
        it = store.get_iter(path)
        print("Selected row: ", store[it][0:])
        sid = store[it][2]
        retval = self.req.play_list_remove(sid)
        print(retval)
        if 'Delete OK' == retval:
            self.play_list_update()

    def result_list_refresh(self):
        if 'topall' == self.req_type:
            data = self.req.top_fetch('all')
        elif 'topzh' == self.req_type:
            data = self.req.top_fetch('zh')
        else:
            data = None

        st = self.res_list_store
        st.clear()

        if None == data:
            return None
        for idx, meta in enumerate(data):
            st.append([idx, meta[1], meta[2], meta[3], meta[4], meta[0]])

    def result_list_add(self):
        path, column = self.res_view.get_cursor()
        if None == path:
            return None

        store = self.res_list_store
        it = store.get_iter(path)
        retval = self.req.play_list_add(store[it][5])
        print(retval)
        if 'Insert OK' == retval:
            self.play_list_update()

    def mv_download(self, sid):
        path = self.req.download(sid)
        if None != path:
            print(path)




if __name__ == '__main__':
    app = stv_class('http://localhost:5000', '2')
    Gtk.main()
