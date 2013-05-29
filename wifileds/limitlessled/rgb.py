import logging
import sys

class RGB:
    def effect(self, effect_name, args=[], effect_options={}):
        effect = sys.modules['wifileds.limitlessled.effects.%s' % effect_name]
        try:
            effect.run(self, *args, **effect_options)
        except AttributeError as e:
            logging.error('Effect "%s" failed due to missing lighting attribute: %s' % (effect_name, e))
            pass

    def __init__(self, parent):
        self.parent = parent
        self.long_pause = parent.long_pause
        self.short_pause = parent.short_pause

        self.color_map = {
            'violet': 0x00,
            'royal_blue': 0x10,
            'baby_blue': 0x20,
            'aqua': 0x30,
            'mint': 0x40,
            'seafoam_green': 0x50,
            'green': 0x60,
            'lime_green': 0x70,
            'yellow': 0x80,
            'yellow_orange': 0x90,
            'orange': 0xA0,
            'red': 0xB0,
            'pink': 0xC0,
            'fusia': 0xD0,
            'lilac': 0xE0,
            'lavendar': 0xF0
        }

    def all_on(self):
        self.parent.send_command(0x22)

    def all_off(self):
        self.parent.send_command(0x21)

    def brightness_up(self):
        self.parent.send_command(0x23)

    def brightness_down(self):
        self.parent.send_command(0x24)

    def mode_up(self):
        self.parent.send_command(0x27)

    def mode_down(self):
        self.parent.send_command(0x28)

    def speed_up(self):
        self.parent.send_command(0x25)

    def speed_down(self):
        self.parent.send_command(0x26)

    def set_color(self, color_name):
        try:
            self.set_color_hex(self.color_map[color_name])
        except KeyError as e:
            raise KeyError('Color not found: %s' % e)

    def set_color_hex(self, color_value):
        self.parent.send_command(0x20, color_value)

    def set_color_wheel(self, percentage):
        if percentage < 0 or percentage > 1:
            raise ValueError('Wheel percentage should be > 0 and < 1.')
        self.parent.send_command(0x20, chr(int(float(255) * percentage)))

    def max_brightness(self):
        for i in range(0, 9):
            self.brightness_up()

    def min_brightness(self):
        for i in range(0, 9):
            self.brightness_down()

    def max_speed(self):
        for i in range(0, 9):
            self.speed_up()

    def min_speed(self):
        for i in range(0, 9):
            self.speed_down()

    def white(self):
        for i in range(0, 20):
            self.mode_down()

    def party_mode(self, number):
        description = {
            1: 'static white color',
            2: 'white color (gradual changes)',
            3: 'all colors (gradual changes)',
            4: 'red/green/blue (gradual changes)',
            5: '7 colors (jump changes)',
            6: '3 colors (jump changes)',
            7: 'red/green (jump changes)',
            8: 'red/blue (jump changes)',
            9: 'blue/green (jump changes)',
            10: 'white color (frequently blinks)',
            11: 'white color (glitters)',
            12: 'red color (frequently blinks)',
            13: 'red color (glitters)',
            14: 'green color (frequently blinks)',
            15: 'green color (glitters)',
            16: 'blue color (frequently blinks)',
            17: 'blue color (glitters)',
            18: 'yellow color (frequently blinks)',
            19: 'yellow color (glitters)',
            20: 'circulation mode',
        }
        print 'Attempting party mode: %s...' % description[number]

        self.white()
        for i in range(1, number):
            self.mode_up()

        print 'Party mode set.'
