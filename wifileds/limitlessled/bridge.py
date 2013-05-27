import socket
import sys
import time

from os.path import dirname

from . import rgb
from . import white

class Bridge:
    def send_command(self, part1, part2=0x00):
        message = bytearray([part1, part2, 0x55])
        for i in range(0, 4):
            self.sock.sendto(message, (self.address, self.port))
            self.short_pause()

    def short_pause(self):
        time.sleep(.015)

    def long_pause(self):
        time.sleep(.1)

    def __init__(self, address='192.168.1.100', port=50000):
        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET,    # Internet
                                  socket.SOCK_DGRAM) # UDP

        self.rgb = rgb.RGB(self)
        self.white = white.White(self)
