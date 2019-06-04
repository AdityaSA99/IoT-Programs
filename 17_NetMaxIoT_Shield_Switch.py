import Netmaxiot
import time

Netmaxiot.pinMode(2,"INPUT")

Netmaxiot.pinMode(5,"OUTPUT")
Netmaxiot.pinMode(6,"OUTPUT")
Netmaxiot.pinMode(7,"OUTPUT")
while 1:
	a=Netmaxiot.digitalRead(2)
	if(a==1):
		print "led on............."
		Netmaxiot.digitalWrite(5,1)
		time.sleep(0.2)
		Netmaxiot.digitalWrite(6,1)
		time.sleep(0.2)
		Netmaxiot.digitalWrite(7,1)
		time.sleep(1)
	else:
		print "led off..............................."
		Netmaxiot.digitalWrite(5,0)
		time.sleep(0.2)
		Netmaxiot.digitalWrite(6,0)
		time.sleep(0.2)
		Netmaxiot.digitalWrite(7,0)
		time.sleep(1)
		