# WifiLEDs Python Library

This package is dedicated to being a cohesive resource point for Wifi LED lighting through Python.

This package currently only contains the API layer for [LimitlessLED bulbs](wifileds/limitlessled) ($16/$19 / bulb), but will soon expand to [LIFX bulbs](http://lifx.co/) ($80 / bulb) which are set to ship in August/September 2013. 

[Philips hue](http://www.meethue.com/) ($60 / bulb) may be looked at into the future, but is currently a bit [expensive](http://www.jon00.me.uk/images/WiFiLEDMatrix.png) for a full house system. Other Python APIs do exist and are linked [here](https://github.com/Q42/hue-libs#python). If any one feels like they want to merge projects, feel free to reach me via GitHub.

Future products that we're looking forward to include:

* From [LimitlessLED](http://whrl.pl/RdBge7):
    * 6W (600 lm) Dual White 2.4Ghz/RF Downlight (June 2013) ~$37 USD
    * 12W (1100 lm) Dual White 2.4Ghz/RF Downlight (June 2013) ~$47 USD
    * 8W Dual White Bulbs (August 2013) ~$17 USD
    * Brighter RGB+White 2.4Ghz/RF Bulbs (October 2013) ~$19 USD
    * New WiFi Bridge (unlimited groups and individual bulb control) (February 2014) ~$17 USD
    * Glass on Black 2.4Ghz/RF In-Wall Switches (October 2014) ~$9 USD

Feel free to add to the list of upcoming products and/or manufactures.

## Binary Examples

See [bin](bin) for example executables for each supported system.

## Module Installation

Install the Python module by running:

```bash
pip install wifileds
```

Then import the module into your code using:

```.py
import wifileds
```

For each submodule's specific usage, read the README.md in the [respective directory](wifileds).

## Coding Examples

See [tests](tests) for example scripts for each supported system.

## Contribution

Feel free to contribute code fixes, new effects, or even new WiFi LED systems via GitHub pull requests.
