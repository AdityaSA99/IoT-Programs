import Netmaxiot
import time

# Netmaxiot.pinMode(2,"INPUT")
# Netmaxiot.pinMode(5,"OUTPUT")
# Netmaxiot.pinMode(6,"OUTPUT")
# Netmaxiot.pinMode(7,"OUTPUT")
a = [2,3,4,5,6,7]
i=0
for i in range(0,6):
	Netmaxiot.pinMode(a[i],"OUTPUT")
i=0
while 1:
	for i in range(0,6):
		print("LED ON ###############################")
		Netmaxiot.digitalWrite(a[i],1)
		time.sleep(0.5)
		print("LED OFF ##############################")
		Netmaxiot.digitalWrite(a[i],0)
		time.sleep(0.5)
# while 1:
# 	a=Netmaxiot.digitalRead(2)
# 	if(a==1):
# 		print "led on............."
# 		Netmaxiot.digitalWrite(5,1)
# 		time.sleep(0.2)
# 		Netmaxiot.digitalWrite(6,1)
# 		time.sleep(0.2)
# 		Netmaxiot.digitalWrite(7,1)
# 		time.sleep(1)
# 	else:
# 		print "led off..............................."
# 		Netmaxiot.digitalWrite(5,0)
# 		time.sleep(0.2)
# 		Netmaxiot.digitalWrite(6,0)
# 		time.sleep(0.2)
# 		Netmaxiot.digitalWrite(7,0)
# 		time.sleep(1)
		