import logging
import sys

class White:
    def effect(self, effect_name, args=[], effect_options={}):
        effect = sys.modules['wifileds.limitlessled.effects.%s' % effect_name]
        try:
            effect.run(self, *args, **effect_options)
        except AttributeError as e:
            logging.error('Effect "%s" failed due to missing lighting attribute: %s' % (effect_name, e))
            pass

    def __init__(self, parent):
        self.parent = parent

    def all_on(self):
        self.parent.send_command(0x35)

    def all_off(self):
        self.parent.send_command(0x39)

    def brightness_up(self):
        self.parent.send_command(0x3C)

    def brightness_down(self):
        self.parent.send_command(0x34)

    def warmer(self):
        self.parent.send_command(0x3E)

    def cooler(self):
        self.parent.send_command(0x3F)

    def zone_on(self, zone):
        if zone == 1:
            self.parent.send_command(0x38)
        elif zone == 2:
            self.parent.send_command(0x3D)
        elif zone == 3:
            self.parent.send_command(0x37)
        elif zone == 4:
            self.parent.send_command(0x32)

    def zone_off(self, zone):
        if zone == 1:
            self.parent.send_command(0x3B)
        elif zone == 2:
            self.parent.send_command(0x33)
        elif zone == 3:
            self.parent.send_command(0x3A)
        elif zone == 4:
            self.parent.send_command(0x36)

    def full_all(self):
        self.all_on()
        self.parent.long_pause()
        self.parent.send_command(0xB5)

    def full_zone(self, zone):
        self.zone_on(zone)
        self.parent.long_pause()

        if zone == 1:
            self.parent.send_command(0xB8)
        elif zone == 2:
            self.parent.send_command(0xBD)
        elif zone == 3:
            self.parent.send_command(0xB7)
        elif zone == 4:
            self.parent.send_command(0xB2)

    def nightlight_all(self):
        self.all_off()
        self.parent.long_pause()
        self.parent.send_command(0xB9)

    def nightlight_zone(self, zone):
        self.zone_off(zone)
        self.parent.long_pause()

        if zone == 1:
            self.parent.send_command(0xBB)
        elif zone == 2:
            self.parent.send_command(0xB3)
        elif zone == 3:
            self.parent.send_command(0xBA)
        elif zone == 4:
            self.parent.send_command(0xB6)

    def max_brightness(self):
        for i in range(0, 10):
            self.brightness_up()

    def min_brightness(self):
        for i in range(0, 10):
            self.brightness_down()

    def max_cool(self):
        for i in range(0, 10):
            self.cooler()

    def max_warm(self):
        for i in range(0, 10):
            self.warmer()
