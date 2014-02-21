import logging
import sys

class RGBW:
    zone_list = [0x42,
                 0x45,
                 0x47,
                 0x49,
                 0x4B,
                ]
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

    def zone_on(self, zone=0):
        # zone 0 = all on
        self.parent.send_command(self.zone_list[zone])

    def zone_off(self, zone=0):
        # zone 0 = all on
        if zone == 0:
            self.parent.send_command(0x41)
        else:
            self.parent.send_command(self.zone_list[zone]+1)

    def all_on(self):
        self.zone_on(0)

    def all_off(self):
        self.zone_off(0)

    def set_brightness(self, brightness, zone=0):
        # RGBW accepts values from 2-27
        if brightness < 2 or brightness > 27:
            raise KeyError('Brightness should be > 1 and < 28.')

        self.zone_on(zone)
        self.parent.long_pause()
        self.parent.send_command(0x4E, chr(int(brightness)))

    def max_brightness(self, zone=0):
        self.set_brightness(27, zone)

    def min_brightness(self, zone=0):
        self.set_brightness(2, zone)

    def mode_up(self):
        self.parent.send_command(0x4D)

    def speed_up(self):
        self.parent.send_command(0x44)

    def speed_down(self):
        self.parent.send_command(0x43)

    def max_speed(self):
        for i in range(0, 9):
            self.speed_up()

    def min_speed(self):
        for i in range(0, 9):
            self.speed_down()

    def set_color(self, color_name, zone=0):
        # If zone == 0, send to all. Otherwise send to specific zone
        try:
            self.set_color_hex(self.color_map[color_name], zone)
        except KeyError as e:
            raise KeyError('Color not found: %s' % e)

    def set_color_hex(self, color_value, zone=0):
        self.zone_on(zone)
        self.parent.long_pause()
        self.parent.send_command(0x40, color_value)

    def set_color_wheel(self, percentage, zone=0):
        if percentage < 0 or percentage > 1:
            raise ValueError('Wheel percentage should be > 0 and < 1.')
        self.set_color_hex(chr(int(float(255) * percentage)), zone)


    def white(self, zone=0):
        # If zone == 0, send to all. Otherwise send to specific zone
        self.parent.send_command(self.zone_list[zone])
        self.parent.long_pause()
        white_zones = [0xC2,
                       0xC5,
                       0xC7,
                       0xC9,
                       0xCB,
                      ]
        self.parent.send_command(white_zones[zone])

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
