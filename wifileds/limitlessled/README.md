These lamps are manufactured in China under the following [brand names](http://board.homeseer.com/showpost.php?p=1063584&postcount=1), depending on country sold:

* [LimitlessLED](http://www.limitlessled.com/)
* [EasyBulb](http://www.easybulb.com/)
* [AppLight](http://www.applight.nl/)
* [AppLamp](http://www.applamp.nl/)
* MiLight
* LEDme
* dekolight
* iLight

# Usage

A connection needs to be made to the bridge:

```.py
led_connection = wifileds.limitlessled.connect('192.168.1.100', 50000)
```

Then one can call actions depending on the lights that will be manipulated:

```.py
led_connection.rgb.all_on()

led_connection.white.all_on()
led_connection.rgbw.all_on()
```

Effects are run by passing the effect name as the 1st parameter and the effect options as shown:

```.py
led_connection.rgb.effect('rainbow_fade', effect_options={'delta': 5})
```

See `tests/limitless.py` for more examples.

# Setup of WiFi Bridge

Connect a PC to the default SSID `wifi-socket`, address the built-in server through your browser [192.168.1.100](http://192.168.1.100) and login as `admin` with a password of `000000`. Change the following settings:

* Wireless Settings
    * Work Type: Set to `Sta`
    * SSID: Set to your existing network SSID (Note: Connect to your 2.4Ghz SSID.)
    * Encryption: Set to existing network encryption mode (Note: AES encryption is not supported.)
    * Key Format: Set as required for your key
    * Encryption Key: Set to your pre-shared key (Note: If using ASCII Key Format, symbols are not accepted.)
* Click Save for this block.

* Network Settings
    * DHCP Enable: Set unchecked
    * Fixed IP Address: The address you wish to use to contact this WiFi Bridge, currently 192.168.1.100
    * Subnet Mask: Set as required, typically 255.255.255.0
    * Gateway Address: Set as required, mine defaults to the same address as the router
    * DNS Address: 8.8.8.8
* Click Save for this block.

* Cycle the power, or click `System` -> `System Restart`. The `LINK` LED light should change to a solid on. If it doesn't work, press the reset button with a paperclip for five seconds and try again from the top.

* You should be able to rejoin your normal network and connect to the bridge through its new IP address.

# Setup of Bulbs

* Turn off the power source.
* Turn on the power source.
* Color Bulbs:
    * Within 3 seconds, press the `mode_up` button. The light should blink 3 times.
* White Bulbs:
    * Within 3 seconds, press the `zone_on` button. The light should blink 3 times.
* Repeat steps for each bulb that needs to be registered.

Notes: 
* All colored lights will be controlled together via the same wireless bridge. If you wish to create different light groups over WiFi, similar to that of the white lights, you will an additional wireless bridge for each group. A new bridge, that is set to allow individual bulb control, is currently slated for a February 2014 release at ~$17 USD.
* You may set up a group of bulbs to be controlled via the WiFi bridge and others via the RF remote. These groups can, but are not required, to intersect.
* I'm unsure if multiple RF remotes can create different groups. (If anyone has information here, that would be useful.)

# Clear Bulb Assignment

* Turn off the power source.
* Turn on the power source.
* Color Bulbs:
    * Within 3 seconds, press and hold the `mode_up` button. The light should blink 6 times.
* White Bulbs:
    * Within 3 seconds, press the `zone_on` button 5 times. The light should blink 6 times.
* Repeat steps for each bulb that needs to be cleared.

# Official Documentation

Since finding official documentation is a bit more difficult than it should be, I've uploaded it [here](http://db.tt/1fsdS6GP).
