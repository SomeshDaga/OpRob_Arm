__author__ = 'someshdaga'

import os
import cmd
import readline
from Servo import *
import traceback
import sys
import subprocess


class Cmd_line(cmd.Cmd):
    def __init__(self):
        proc = subprocess.Popen("ls /dev/*[uU][sS][bB]*", stdout = subprocess.PIPE, shell = True)
        out, err = proc.communicate()
        usb_list = out.split("\n")
        for usb in usb_list:
            try:
                if find_servos(USB2Dynamixel_Device(usb, 57600)):
                    servos = find_servos(USB2Dynamixel_Device(usb, 57600))
                elif find_servos(USB2Dynamixel_Device(usb, 100000)):
                    servos = find_servos(USB2Dynamixel_Device(usb, 100000))
                else:
                    continue

                if len(servos) == 1:
                    global grasper_dyn
                    global grasper_servo
                    grasper_dyn = USB2Dynamixel_Device( usb )
                    grasper_servo = Robotis_Servo( grasper_dyn, servos[0] )
                elif len(servos) == 2:
                    global upper_arm_dyn
                    global upper_arm_servo
                    global shoulder_servo
                    upper_arm_dyn = USB2Dynamixel_Device(usb)
                    upper_arm_servo = Robotis_Servo(upper_arm_dyn, servos[0])
                    shoulder_servo = Robotis_Servo(upper_arm_dyn, servos[1])
                else:
                    pass
            except:
                continue

        self.initialize_servos( )

    def initialize_servos(self):
        pass


if __name__ == "__main__":
    cmd_l = Cmd_line( )