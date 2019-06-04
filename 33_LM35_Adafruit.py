#!/usr/bin/python

import Netmaxiot
from Adafruit_IO import Client
import Adafruit_DHT
import os
import time
import requests
DELAY_TIME = 8



ADAFRUIT_IO_USERNAME = 'AdityaSA99'
ADAFRUIT_IO_KEY = '439d545f8aca4bea99ba3f4bcbceb081'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
Voltage0 = aio.feeds('lm35.voltage0')
Voltage1 = aio.feeds('lm35.voltage1')
Temp0 = aio.feeds('lm35.temp0')
Temp1 = aio.feeds('lm35.temp1')
###################################################


while True:
    #################################
    PIN0 = Netmaxiot.analogRead(0)
    PIN1 = Netmaxiot.analogRead(1)
    vol0 = ((PIN0*4.88)/1000)
    vol1 = ((PIN1*4.88)/1000)
    temp0 = vol0/10
    temp1 = vol1/10
##################################################33
    print '> Voltage 0 : ', str(float(vol0))
    aio.send(Voltage0.key, float(vol0))
    print '> Voltage 1 : ', str(float(vol1))
    aio.send(Voltage1.key, float(vol1))
    print '> Temp 0 : ', str(float(temp0))
    aio.send(Temp0.key, float(temp0))
    print '> Temp 1 : ', str(float(temp1))
    aio.send(Temp1.key, float(temp1))
    time.sleep(DELAY_TIME)