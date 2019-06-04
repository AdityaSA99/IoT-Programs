#!/usr/bin/env python
import Netmaxiot
import requests
from time import sleep

def read_volt():
	PIN1 = Netmaxiot.analogRead(1)
	vol1 = ((PIN1*4.88))
	temp = ((vol1/5000)*100)
	print(PIN1)
	print (vol1)
	print "The Luminocity is %0.2f"%(temp)
	payload = {'Luminocity': temp}
	return payload
##################################################33

while True:
	try:
		r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=A1E-Jn28yhVUAyTVZWVHaiLXMkw76N8Tn3', data=read_volt())
		print('Posting voltage in Ubidots')
		print(read_volt())
		sleep(1)
	except:
		print('Sada temperatures post nahin hoyaa in Ubidots check karo :( ')     
		sleep(2)