#!/usr/bin/env python
import time

from optparse import OptionParser

import wifileds

if __name__=="__main__":
    parser = OptionParser()
    parser.add_option('-a', '--address', default='192.168.1.100', help='wifi block ip address')
    parser.add_option('-p', '--port', type='int', default=50000, help='wifi block port address')
    (options, args) = parser.parse_args()

    print 'Create a connection to the wifi bridge...'
    led_connection = wifileds.limitlessled.connect(options.address, options.port)

    print 'Turn on all color lights...'
    led_connection.rgb.all_on()

    print 'Fade lights all the way up...'
    led_connection.rgb.effect('fade_up')

    print 'Ensure they cannot get brighter...'
    time.sleep(1)
    led_connection.rgb.effect('fade_up')

    print 'Change to lilac...'
    led_connection.rgb.set_color('lilac')
    time.sleep(1)

    print 'Change to yellow...'
    led_connection.rgb.set_color('yellow')
    time.sleep(1)

    print 'Fade lights all the way down...'
    led_connection.rgb.effect('fade_down')

    print 'Ensure they cannot get dimmer...'
    time.sleep(1)
    led_connection.rgb.effect('fade_down')

    print 'Return to full brightness...'
    led_connection.rgb.effect('fade_up')

    print 'Colorful strobe effect. Can be customized to select only certain colors...'
    led_connection.rgb.effect('colorful_strobe')

    print 'Wave pattern with the fading of the lights...'
    led_connection.rgb.effect('fade_up')
    led_connection.rgb.effect('fade_down')
    led_connection.rgb.effect('fade_up')
    led_connection.rgb.effect('fade_down')

    print 'Police flashers effects. Colors can be customized or fully random...'
    led_connection.rgb.effect('police_flashers')

    print 'Pulsating yellow factory flashers. Colors can be customized or fully random...'
    led_connection.rgb.effect('pulsating_swells', effect_options={'duration': 15})

    print 'Rainbow fade. Speed of change and quickness can be customized...'
    led_connection.rgb.effect('rainbow_fade', effect_options={'delta': 5})

    print 'Strobe effect based on the previously set color...'
    led_connection.rgb.effect('strobe', effect_options={'duration': 5})

    print 'Flash the lights a final time...'
    led_connection.rgb.all_off()
    time.sleep(1)
    led_connection.rgb.all_on()

    print 'Done.'
