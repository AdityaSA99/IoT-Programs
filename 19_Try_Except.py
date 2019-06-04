#!/usr/bin/env python

import Netmaxiot
import time
Netmaxiot.pinMode(5,"OUTPUT")
Netmaxiot.pinMode(6,"OUTPUT")
Netmaxiot.pinMode(7,"OUTPUT")
try:
	while 1:
		print("led on................................")
		Netmaxiot.digitalWrite(5,1)
		time.sleep(0.2)
		Netmaxiot.digitalWrite(6,1)
		time.sleep(0.2)
		Netmaxiot.digitalWrite(7,1)
		time.sleep(1)

		print("led off...............................")
		Netmaxiot.digitalWrite(5,0)
		time.sleep(0.2)
		Netmaxiot.digitalWrite(6,0)
		time.sleep(0.2)
		Netmaxiot.digitalWrite(7,0)
		time.sleep(1)
except:
	print("Error !!! Please Check Your Connections")
