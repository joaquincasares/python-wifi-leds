#!/usr/bin/env python
import time

from optparse import OptionParser

import wifileds

if __name__=="__main__":
    parser = OptionParser()
    parser.add_option('-a', '--address', default='192.168.1.100', help='wifi block ip address')
    parser.add_option('-p', '--port', type='int', default=50000, help='wifi block port address')
    (options, args) = parser.parse_args()

    led_connection = wifileds.limitlessled.connect(options.address, options.port)

    led_connection.rgb.all_on()

    # led_connection.rgb.effect('fade_up')
    # time.sleep(1)
    # led_connection.rgb.effect('fade_up')

    # led_connection.rgb.set_color('lilac')
    # led_connection.rgb.set_color('yellow')

    # led_connection.rgb.effect('rainbow_fade', effect_options={'delta': 5})

    # led_connection.rgb.effect('fade_down')
    # time.sleep(1)
    # led_connection.rgb.effect('fade_down')

    # led_connection.rgb.effect('strobe', effect_options={'duration': 5})

    # led_connection.rgb.all_off()
    # time.sleep(1)
    # led_connection.rgb.all_on()

    for i in range(1,21):
        led_connection.rgb.party_mode(i)
        time.sleep(5)
