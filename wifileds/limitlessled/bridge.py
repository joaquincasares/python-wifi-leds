import logging
import socket
import sys
import time

from os.path import dirname

from . import rgb
from . import white
from . import rgbw

class Bridge:
    def send_command(self, part1, part2=0x00):
        message = bytearray([part1, part2, 0x55])

        # Send message multiple times to simulate a button press
        for i in range(0, 3):
            try:
                if self.protocol == 'udp':
                    self.sock.sendto(message, (self.address, self.port))
                elif self.protocol == 'tcp':
                    self.sock.send(message)

                    # Catch and discard the response
                    self.sock.recv(1024)
            except Exception as e:
                # Reconnect on failures
                self.create_connection()

                logging.error(e)

            # Keep the messages from flooding the device
            self.short_pause()

    def short_pause(self):
        # Hand-tuned value that gets decent performance of speed to miss ratios
        time.sleep(self.short_pause_duration)

    def long_pause(self):
        # Useful for nightlight features that require a long press
        time.sleep(self.long_pause_duration)

    def create_connection(self):
        if self.protocol == 'udp':
            self.sock = socket.socket(socket.AF_INET, # Internet
                                      socket.SOCK_DGRAM) # UDP
        elif self.protocol == 'tcp':
            self.sock = socket.socket(socket.AF_INET, # Internet
                                      socket.SOCK_STREAM) # TCP
            self.sock.connect((self.address, self.port))
        else:
            raise TypeError('Protocol "%s" is not a known protocol.' % self.protocol)

    def __init__(self, address='192.168.1.100', port=50000,
                 short_pause_duration=0.025,
                 long_pause_duration=0.1,
                 protocol='udp'):

        self.address = address
        self.port = port
        self.short_pause_duration = short_pause_duration
        self.long_pause_duration = long_pause_duration
        self.protocol = protocol

        self.create_connection()

        self.rgb = rgb.RGB(self)
        self.white = white.White(self)
        self.rgbw = rgbw.RGBW(self)
