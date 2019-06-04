import time
from Adafruit_IO import Client
from w1thermsensor import W1ThermSensor

DELAY_TIME = 8
##########################
import Adafruit_DHT
sensor = W1ThermSensor()
pin = 4
sensor1 = Adafruit_DHT.DHT11
pin = 17
###################################
ADAFRUIT_IO_USERNAME = 'AdityaSA99'
ADAFRUIT_IO_KEY = '439d545f8aca4bea99ba3f4bcbceb081'

##################################################
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

tempc = aio.feeds('ds18b20')
temperature = aio.feeds('mytemperature')
humidity = aio.feeds('myhumidity')
################################################

while True:
    humidity_data, temperature_data = Adafruit_DHT.read_retry(sensor1, pin)
    tempcelcius_data = sensor.get_temperature()
    print '> ds18b20_temp: ', float(tempcelcius_data)
    aio.send(tempc.key, float(tempcelcius_data))
    print '> Temperature: ', float(temperature_data)
    aio.send(temperature.key, float(temperature_data))
    print '> Humidity :', float(humidity_data)
    aio.send(humidity.key, float(humidity_data))
    time.sleep(DELAY_TIME)
