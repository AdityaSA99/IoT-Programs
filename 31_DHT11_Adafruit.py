
# pip install Adafruit_IO
# line 66, in _warn_if_setuptools_outdated
# setuptools_scm.version.SetuptoolsOutdatedWarning: your setuptools is too old (<12)
# run pip install -U pip setuptools before installing library


import time
from Adafruit_IO import Client
DELAY_TIME = 8
##########################
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 17
###################################
ADAFRUIT_IO_USERNAME = 'AdityaSA99'
ADAFRUIT_IO_KEY = '439d545f8aca4bea99ba3f4bcbceb081'

##################################################
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
temperature = aio.feeds('mytemperature')
humidity = aio.feeds('myhumidity')
################################################

while True:
    humidity_data, temperature_data = Adafruit_DHT.read_retry(sensor, pin)
    print '> Temperature: ', float(temperature_data)
    aio.send(temperature.key, float(temperature_data))
    print '> Humidity :', float(humidity_data)
    aio.send(humidity.key, float(humidity_data))
    time.sleep(DELAY_TIME)
