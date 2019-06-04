#!/usr/bin/python


# import Adafruit_DHT
import os
import time
import requests
from w1thermsensor import W1ThermSensor

#################################
sensor = W1ThermSensor()
pin = 4
###############################
def read_temp():
    # humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temp_c = sensor.get_temperature()
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    print temp_c
    time.sleep(0.3)
    print temp_f
    payload = {'Temp_Celcius': temp_c, 'Temp_Fahrenheit': temp_f}
    return payload

##################################################33

while True:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=A1E-Jn28yhVUAyTVZWVHaiLXMkw76N8Tn3', data=read_temp())
            print('Posting Temperature and Humidity in Ubidots')
            print(read_temp())
            time.sleep(3)
        except:
            print('Error Posting Temperature !!! Please Check    :( ')     
            time.sleep(10)

