#!/usr/python3

from util.stv_request import stv_request_class as stv_req
from util.stv_ui import stv_ui_class as stv_app

class stv_class(object):
    def __init__(self):
        self.UI_bind()
        self.SVR_bind()
        pass

    def UI_bind(self):
        self.app = stv_app()

    def SVR_bind(self):
        self.req = stv_req()


if __name__ == '__main__':
    cli = stv_class()
