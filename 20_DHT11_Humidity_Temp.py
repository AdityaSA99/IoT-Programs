#!/usr/bin/env python


# To install Adafruit DHT Library
# cd /home/pi 
# sudo apt-get install build-essential python-dev python-openssl
# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# cd Adafruit_Python_DHT
# sudo python setup.py install


import Adafruit_DHT
from time import sleep
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11
pin = 22

while 1:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print humidity
        print temperature
        print "Aditya #######################"
        sleep(2)
    else:
        print('Failed to get reading. Try again!')
