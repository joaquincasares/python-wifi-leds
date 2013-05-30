import logging
import socket
import sys
import time

from os.path import dirname

from . import rgb
from . import white

class Bridge:
    def send_command(self, part1, part2=0x00):
        message = bytearray([part1, part2, 0x55])

        # Send message multiple times to simulate a button press
        for i in range(0, 3):
            try:
                self.sock.sendto(message, (self.address, self.port))
            except Exception as e:
                # Reconnect on failures
                self.sock = socket.socket(socket.AF_INET,    # Internet
                                          socket.SOCK_DGRAM) # UDP
                logging.error(e)

            # Keep the messages from flooding the device
            self.short_pause()

    def short_pause(self):
        # Hand-tuned value that gets decent performance of speed to miss ratios
        time.sleep(self.short_pause_duration)

    def long_pause(self):
        # Useful for nightlight features that require a long press
        time.sleep(self.long_pause_duration)

    def __init__(self, address='192.168.1.100', port=50000,
                 short_pause_duration=0.025,
                 long_pause_duration=0.1):

        self.address = address
        self.port = port
        self.short_pause_duration = short_pause_duration
        self.long_pause_duration = long_pause_duration

        self.sock = socket.socket(socket.AF_INET,    # Internet
                                  socket.SOCK_DGRAM) # UDP

        self.rgb = rgb.RGB(self)
        self.white = white.White(self)
