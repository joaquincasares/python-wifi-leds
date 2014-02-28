#!/usr/bin/env python
try:
      from setuptools import setup
except:
      from distutils.core import setup

setup(name='wifileds',
      version='1.0.6',
      description='Library for multiple WiFi LED vendors.',
      long_description=open('README.md').read(),
      author='Joaquin Casares',
      author_email='joaquin.casares AT gmail.com',
      url='http://github.com/joaquincasares/python-wifi-leds',
      packages=['wifileds', 
                'wifileds.limitlessled', 
                'wifileds.limitlessled.effects'],
      package_data={'': ['README.md']},
      keywords='wifi led leds l.e.d. light emitting diodes lights lamps bulbs lighting home automation network mesh future LimitlessLED EasyBulb AppLight AppLamp MiLight LEDme dekolight iLight Philips hue LIFX'
     )
