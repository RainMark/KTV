#!/usr/bin/python3


import qrcode
from random import randint


class stv_qr_class(qrcode.QRCode):
    def __init__(self, **kw):
        super().__init__(version=1, box_size=4, border=1)
        self.machine = kw['machine']
        self.seq_length = kw['seq_length']
        self.save_path = kw['save_path']

    def prepare_data(self):
        self.add_data(str(self.machine) + '@' + self.random_sequence())

    def save_image(self):
        self.make(fit=True)
        self.make_image().save(self.save_path)

    def random_sequence(self):
        seq = str()
        for i in range(10):
            seq += str(randint(0, self.seq_length - 1))

        return seq

if __name__ == '__main__':
    qr = stv_qr_class(machine=2,
                      seq_length=10,
                      save_path='/tmp/stv_qr.png')

    qr.prepare_data()
    qr.save_image()
