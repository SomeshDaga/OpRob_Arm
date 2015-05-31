from Servo import *
import math
import time
import sys
import os

sys.stdout.write("USB serial devices found:\n")
os.system("ls /dev/tty*[uU]sb*")
sys.stdout.write("Choose the dev_name for Arm Servo: ")
dev_name = raw_input()

dyn = USB2Dynamixel_Device(dev_name)

#find_servos(dyn)
#recover_servo(dyn)


serv = Robotis_Servo( dyn, 2)
#
#
serv.move_angle(math.radians(30))
#print serv.recieve_reply()
