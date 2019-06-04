#!/usr/bin/python

import Netmaxiot
import Adafruit_DHT
import os
import time
import requests
#################################
def read_volt():
        PIN0 = Netmaxiot.analogRead(0)
        # PIN1 = Netmaxiot.analogRead(1)
        # PIN2 = Netmaxiot.analogRead(2)
        # PIN3 = Netmaxiot.analogRead(3)
        vol0 = ((PIN0*4.88))
        temp = vol0/10
        # vol1 = ((PIN1*4.88)/1000)
        # vol2 = ((PIN2*4.88)/1000)
        # vol3 = ((PIN3*4.88)/1000)
        print(PIN0)
        print (vol0)
        print "The Temperature is %0.2f"%(temp)
        # print (vol1)
        # print (vol2)
        # print (vol3)
        payload = {'Voltage-0': vol0}
        # payload = {'Voltage-0': vol0, 'Voltage-1': vol1, 'Voltage-2': vol2, 'Voltage-3': vol3}
        return payload
##################################################33

while True:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=A1E-Jn28yhVUAyTVZWVHaiLXMkw76N8Tn3', data=read_volt())
            print('Posting voltage in Ubidots')
            print(read_volt())
            time.sleep(1)
        except:
            print('Sada temperatures post nahin hoyaa in Ubidots check karo :( ')     
            time.sleep(2)

