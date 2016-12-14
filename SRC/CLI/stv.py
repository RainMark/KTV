#!/usr/python3

import os, signal, time, sys, gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gst', '1.0')
from gi.repository import Gtk, Gdk, GObject, Gst, GdkPixbuf

sys.path.append(os.path.join(os.getcwd(), 'util'))
from stv_request import stv_request_class
from stv_video import stv_video_player_class
from stv_qr import stv_qr_class

global app

class stv_signal_handler(object):
    def stv_exit(self, *args):
        app.player.exit()
        Gtk.main_quit(*args)

    def stv_rank_decorator(func):
        def wrapper(*args, **kw):
            app.handler.stv_back()
            box = app.box_rank
            child = box.get_children()
            box.remove(child[0])
            box.add(app.box_top50)
            app.stack_box = box
            app.stack_box_child = child[0]
            app.restored = False
            func(*args, **kw)
            app.result_list_refresh()
        return wrapper

    @stv_rank_decorator
    def stv_rank_all(self, *args):
        app.req_type = 'all'

    @stv_rank_decorator
    def stv_rank_zh(self, *args):
        app.req_type = 'zh'

    @stv_rank_decorator
    def stv_rank_en(self, *args):
        app.req_type = 'en'

    @stv_rank_decorator
    def stv_rank_new(self, *args):
        app.req_type = 'new'

    @stv_rank_decorator
    def stv_rank_week(self, *args):
        app.req_type = 'week'

    @stv_rank_decorator
    def stv_rank_month(self, *args):
        app.req_type = 'month'

    def stv_recommend_decorator(func):
        def wrapper(*args, **kw):
            app.handler.stv_back()
            box = app.box_recommend
            child = box.get_children()
            box.remove(child[0])
            box.add(app.box_top50)
            app.stack_box = box
            app.stack_box_child = child[0]
            app.restored = False
            func(*args, **kw)
            app.result_list_refresh()
        return wrapper

    @stv_recommend_decorator
    def stv_recommend_rock(self, *args):
        app.req_type = 'rock'

    @stv_recommend_decorator
    def stv_recommend_popular(self, *args):
        app.req_type = 'popular'

    @stv_recommend_decorator
    def stv_recommend_random(self, *args):
        app.req_type = 'random'

    @stv_recommend_decorator
    def stv_recommend_comment(self, *args):
        app.req_type = 'comment'

    @stv_recommend_decorator
    def stv_recommend_guess(self, *args):
        app.req_type = 'guess'

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
        app.top_menu.hide()
        app.result_list_refresh()

    def stv_result_add(self, *args):
        app.top_menu.hide()
        app.play_list_add(app.top_menu.view)

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
        app.in_mv = False

    def stv_mv_play(self, *args):
        if Gst.State.PLAYING == app.player.state:
            app.player.pause()
            app.bt_play.set_image(app.pause_img)

        elif Gst.State.PAUSED == app.player.state:
            app.player.play()
            app.bt_play.set_image(app.play_img)

        elif Gst.State.NULL == app.player.state:
            ok = app.play_list_play()
            if ok:
                app.bt_play.set_image(app.play_img)

    def stv_mv_next(self, *args):
        app.play_list_next()

    def stv_find(self, *args):
        app.tmp_star_store.clear()
        app.tmp_song_store.clear()
        app.find_menu.menu.popup()

    def stv_qr_show(self, *args):
        app.qr_img.set_from_file('/tmp/stv_qr.png')
        app.qr_menu.menu.popup()

    def stv_search_changed(self, *args):
        key = app.entry_search.get_text()
        if 0 == len(key):
            return None
        app.popover_search(key)

    def stv_search_show(self, *args):
        key = app.entry_search.get_text()
        if 0 == len(key):
            return None
        app.find_menu.menu.hide()
        if app.in_mv:
            self.stv_mv_hide(*args)
        app.stack.set_visible_child_name('page2')
        app.box_search(key)

    def stv_search_star(self, *args):
        print('Row changed')
        app.view_search()

    def stv_filter_star_type(self, widget, event):
        print('stv_filter_star_type ', dir(widget))
        print(widget.__class__)
        print(widget.get_name())
        print(widget.get_children())

class stv_popover(object):
    def __init__(self, menu):
        self.menu = menu

    def show_all(self, widget, event):
        print(widget)
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
            self.view = widget

    def hide(self):
        self.menu.hide()

    def connect_signal(self, obj, signal):
        obj.connect(signal, self.show_all)


class stv_class(object):
    def __init__(self, server, machine):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.handler = stv_signal_handler()
        self.UI_build()
        self.check_network(server, machine)
        if self.req.online:
            self.play_list_update()
        self.restored = True
        self.req_type = 'topall'
        self.last_operation = None
        self.in_mv = False

    def check_network(self, svr, mach):
        self.SVR_init(svr, mach)
        self.QR = stv_qr_class(machine=mach,
                               seq_length=10,
                               save_path='/tmp/stv_qr.png')
        self.QR.prepare_data()
        self.QR.save_image()
        self.req.sequence_init(self.QR.seq)

    def UI_build(self):
        self.builder           = Gtk.Builder()
        self.builder.add_from_file("resources/glade/main.xml")

        self.play_menu         = stv_popover(self.builder.get_object('play_menu'))
        self.top_menu          = stv_popover(self.builder.get_object('top_menu'))
        self.find_menu         = stv_popover(self.builder.get_object('find_menu'))
        self.qr_menu           = stv_popover(self.builder.get_object('qr_menu'))

        self.titlebar          = self.builder.get_object('headerbar')
        self.window            = self.builder.get_object('window')
        self.stack             = self.builder.get_object('st_context')

        self.box_main          = self.builder.get_object('box_main')
        self.box_menu          = self.builder.get_object('box_menu')
        self.box_phrase        = self.builder.get_object('box_phrase')
        self.box_disp          = self.builder.get_object('box_disp')
        self.box_ctrl          = self.builder.get_object('box_ctrl')
        self.box_top50         = self.builder.get_object('box_top50')
        self.box_rank          = self.builder.get_object('box_rank')
        self.box_recommend     = self.builder.get_object('box_recommend')

        self.play_store        = self.builder.get_object('lt_play')
        self.history_store     = self.builder.get_object('lt_history')
        self.comment_store     = self.builder.get_object('lt_comment')
        self.top_store         = self.builder.get_object('lt_top')
        self.tmp_star_store    = self.builder.get_object('lt_tmp_star')
        self.tmp_song_store    = self.builder.get_object('lt_tmp_song')
        self.star_store        = self.builder.get_object('lt_star')
        self.song_store        = self.builder.get_object('lt_song')

        self.play_view         = self.builder.get_object('tv_play')
        self.history_view      = self.builder.get_object('tv_history')
        self.top_view          = self.builder.get_object('tv_top')
        self.star_view         = self.builder.get_object('tv_star')
        self.song_view         = self.builder.get_object('tv_song')

        self.grid_mv           = self.builder.get_object('grid_mv')
        self.sc_comment        = self.builder.get_object('sc_comment')
        self.disp_area         = self.builder.get_object('disp_area')
        self.bt_mv_back        = self.builder.get_object('bt_mv_back')
        self.bt_play           = self.builder.get_object('bt_play')
        self.bt_qr             = self.builder.get_object('bt_qr')

        self.play_img          = self.builder.get_object('bt_play_img')
        self.pause_img         = self.builder.get_object('bt_pause_img')
        self.qr_img            = self.builder.get_object('qr_img')

        self.entry_search      = self.builder.get_object('entry_search')

        self.player            = stv_video_player_class(self.handler, self.handler.stv_mv_next)

        # Setup control buttons
        self.box_disp.set_valign(Gtk.Align.END)
        self.box_disp.set_halign(Gtk.Align.START)
        self.grid_mv.attach(self.box_ctrl, 1, 0, 1, 1)
        self.window.set_titlebar(self.titlebar)

        # Setup right click popover menu
        self.play_menu.connect_signal(self.play_view, "button-press-event")
        self.top_menu.connect_signal(self.top_view, "button-press-event")
        self.top_menu.connect_signal(self.history_view, "button-press-event")
        self.top_menu.connect_signal(self.song_view, "button-press-event")
        self.builder.connect_signals(self.handler)

        self.UI_apply_css()
        self.window.set_size_request(1110, 760)
        self.window.show_all()
        # In self.player, get_xid() can be called after window.show_all()
        self.player.set_xid(self.disp_area)
        self.player.ready(os.path.abspath('resources/blank.mp4'))
        self.player.stop()

    def UI_apply_css(self):
        self.style_provider = Gtk.CssProvider()
        self.style_provider.load_from_path('resources/glade/main.css')
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),
                                                 self.style_provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def SVR_init(self, svr, mach):
        self.req = stv_request_class(svr, mach)

    def play_list_first_row_id(self):
        store = self.play_store
        it = store.get_iter_first()
        if None == it:
            return None

        return store[it][2]

    def play_list_update(self):
        data = self.req.play_list_fetch()
        store = self.play_store
        if None != data:
            store.clear()
            for idx, meta in enumerate(data):
                store.append([idx, meta[1], meta[0]])
        self.his_list_update()

    def his_list_update(self):
        data = self.req.his_list_fetch()
        store = self.history_store
        if None != data:
            store.clear()
            for idx, meta in enumerate(data):
                store.append([idx, meta[1], meta[0]])

    def play_list_move(self):
        path, column = self.play_view.get_cursor()
        if None == path:
            return None

        store = self.play_store
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

        store = self.play_store
        it = store.get_iter(path)
        print("Selected row: ", store[it][0:])
        sid = store[it][2]
        retval = self.req.play_list_remove(sid)
        print(retval)
        if 'Delete OK' == retval:
            self.play_list_update()

    def result_list_refresh(self):
        if None == self.req_type:
            return None

        data = self.req.top_fetch(self.req_type)
        st = self.top_store
        st.clear()

        if None == data:
            return None

        for idx, meta in enumerate(data):
            st.append([idx, meta[1], meta[2], meta[3], meta[4], meta[0]])

    def play_list_add(self, view):
        path, column = view.get_cursor()
        if None == path:
            return None

        store = view.get_model()
        print(store)
        it = store.get_iter(path)
        if view == self.history_view:
            i = 2
        else:
            i = 5
        retval = self.req.play_list_add(store[it][i])
        print(retval)
        if 'Insert OK' == retval:
            self.play_list_update()

    def play_list_play(self):
        sid = self.play_list_first_row_id()
        if None == sid:
            return False

        path = self.req.download(sid)
        print(path)
        if None != path:
            self.player.ready(path)
            self.player.play()
            self.bt_play.set_image(self.play_img)
            self.comment_fetch()
            return True
        return False

    def play_list_stop(self):
        if Gst.State.NULL != self.player.state:
            self.player.stop()
            self.bt_play.set_image(self.pause_img)

    def play_list_next(self):
        self.play_list_stop()

        sid = self.play_list_first_row_id()
        if None == sid:
            return False

        retval = self.req.play_list_remove(sid)
        if 'Delete OK' == retval:
            self.play_list_update()
            self.play_list_play()
            return True

        return False

    def comment_fetch(self):
        sid = self.play_list_first_row_id()
        if None == sid:
            return False

        data = self.req.comment_fetch(sid)
        if None == data:
            return False

        print(data)
        st = self.comment_store
        st.clear()
        for meta in data:
            st.append([meta])

    def popover_search(self, key):
        use_unicode = (ord(key[0]) > ord('z'))
        if use_unicode:
            data = self.req.search_singer_by_fullname(key)
        else:
            data = self.req.search_singer_by_abridge(key)

        if None == data:
            return False

        st = self.tmp_star_store
        st.clear()
        for meta in data[:4]:
            print(meta)
            st.append([meta[1], meta[0]])

        if use_unicode:
            data = self.req.search_song_by_fullname(key)
        else:
            data = self.req.search_song_by_abridge(key)

        if None == data:
            return False

        st = self.tmp_song_store
        st.clear()
        for meta in data[:4]:
            # print(meta)
            st.append([meta[1], meta[0]])

    def box_search(self, key):
        use_unicode = (ord(key[0]) > ord('z'))
        if use_unicode:
            data = self.req.search_singer_by_fullname(key)
        else:
            data = self.req.search_singer_by_abridge(key)

        if None == data:
            return False

        st = self.star_store
        st.clear()
        for meta in data:
            print(meta)
            image = self.req.album_fetch(meta[0])
            if None == image:
                continue
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(image, 80, 80)
            st.append([pixbuf, meta[1], meta[0]])

        if use_unicode:
            data = self.req.search_song_by_fullname(key)
        else:
            data = self.req.search_song_by_abridge(key)

        if None == data:
            return False

        st = self.song_store
        st.clear()
        for idx, meta in enumerate(data):
            st.append([idx, meta[1], meta[2], meta[3], meta[4], meta[0]])

    def view_search(self):
        path, column = self.star_view.get_cursor()
        if None == path:
            return None

        self.song_store.clear()
        st = self.star_store
        it = st.get_iter(path)
        data = self.req.singer_song_fetch(st[it][2])
        if None == data:
            return None

        st = self.song_store
        for idx, meta in enumerate(data):
            st.append([idx, meta[1], meta[2], meta[3], meta[4], meta[0]])


def init_env(tmp_path = '/tmp/stv'):
    if not os.path.isdir(tmp_path):
        os.mkdir(tmp_path)

if __name__ == '__main__':
    init_env()
    app = stv_class('http://localhost:5000', '1')
    Gtk.main()
