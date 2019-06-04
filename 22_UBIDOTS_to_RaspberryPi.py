#!/usr/bin/python


import Adafruit_DHT
import os
import time
import requests

#################################
sensor = Adafruit_DHT.DHT11
pin = 17
###############################
def read_temp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print humidity
    time.sleep(0.3)
    print temperature
    payload = {'Aditya_Temperature': temperature, 'Aditya_Humidity': humidity}
    return payload

##################################################33

while True:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=A1E-Jn28yhVUAyTVZWVHaiLXMkw76N8Tn3', data=read_temp())
            print('Posting Temperature and Humidity in Ubidots')
            print(read_temp())
            time.sleep(3)
        except:
            print('Error Posting Temperature and Humidity !!! Please Check    :( ')     
            time.sleep(10)

