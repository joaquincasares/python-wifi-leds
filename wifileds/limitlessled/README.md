These lamps are manufactured in China under the following brand names, depending on country sold:

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
```

Effects are run by passing the effect name as the 1st parameter and the effect options as shown:

```.py
led_connection.rgb.effect('rainbow_fade', effect_options={'delta': 5})
```

See `tests/limitless.py` for more examples.
