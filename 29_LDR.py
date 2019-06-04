#!/usr/bin/env python
import Netmaxiot
from time import sleep
while True:
        myvalue = Netmaxiot.analogRead(1)
        sleep(2)
        voltage = myvalue*4.88
        print "----------"
        print "the voltage in mv is == %0.2f mv" %(voltage)
        print "-------------------"
        light=(voltage/5000)*100

        print "the room Ambient is == %0.2f percent" %(light)
        print "----------"
        print "----------"
