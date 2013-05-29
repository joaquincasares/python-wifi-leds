These lamps are manufactured in China under the following brand names, depending on country sold:

* Limitless LED
* dekolight
* iLight
* applight
* applamp
* LEDme
* EasyBulb
* MiLight

# Usage

A connection needs to be made to the bridge:

    ```py
    led_connection = wifileds.limitlessled.connect('192.168.1.100', 50000)
    ```

Then one can call actions depending on the lights that will be manipulated:

    ```py
    led_connection.rgb.all_on()

    led_connection.white.all_on()
    ```
