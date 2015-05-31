#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
from Servo import *
import math
import time
import threading
import HandGui

import spidev
import time
import os

class controlPanelGUI(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initializeServo()
        self.initializeGui()



    def initializeGui(self):
        self.grid()
        self.initializeHand()
        self.initializeWrist()

        #Frame Specifics
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry('800x400+100+100')    
        self.angleEntryHand.focus_set()
        self.angleEntryHand.selection_range(0, Tkinter.END)



    def initializeHand(self):
        #Angle Entry Box
        self.angleEntryVariableHand = Tkinter.StringVar()
        self.angleEntryHand = Tkinter.Entry(self,
            textvariable=self.angleEntryVariableHand)
        self.angleEntryHand.grid(column=0,row=0,sticky='EW')
        self.angleEntryHand.bind("<Return>", self.Hand_OnPressEnter_Angle)
        self.angleEntryVariableHand.set(u"Enter Angle Here")

        #Angle Entry Box
        #self.angleEntryVariableHand = Tkinter.StringVar()
        #self.angleEntryHand = Tkinter.Entry(self,
         #   textvariable=self.angleEntryVariableHand)
       #self.angleEntryHand.grid(column=0,row=0,sticky='EW')
        #self.angleEntryHand.bind("<Return>", self.Hand_OnJoyStick_Angle)
        #self.angleEntryVariableHand.set(u"Enter Angle Here")

        #Angle Entry Button
        angleEnterButtonHand = Tkinter.Button(self,text=u"Enter",
            command=self.Hand_OnPressButton_Angle)
        angleEnterButtonHand.grid(column=1,row=0)

        #Angle Info Box
        self.angleLabelVariableHand = Tkinter.StringVar()
        angleLabelHand = Tkinter.Label(self,textvariable=self.angleLabelVariableHand,
                              anchor="w",fg="white",bg="blue")
        angleLabelHand.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.angleLabelVariableHand.set(u"Angle: "+str(round(float(math.degrees(grasperServ.read_angle())),2))+" Deg")

        #Load Info Box
        self.loadLabelVariableHand = Tkinter.StringVar()
        loadLabelHand = Tkinter.Label(self,textvariable=self.loadLabelVariableHand,
                              anchor="w",fg="white",bg="red")
        loadLabelHand.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.loadLabelVariableHand.set(u"Load: "+str(int(grasperServ.read_load()))+" Units")

        #Temp Info Box
        self.tempLabelVariableHand = Tkinter.StringVar()
        tempLabelHand = Tkinter.Label(self,textvariable=self.tempLabelVariableHand,
                              anchor="w",fg="white",bg="purple")
        tempLabelHand.grid(column=0,row=3,columnspan=2,sticky='EW')
        self.tempLabelVariableHand.set(u"Temp: "+str(int(grasperServ.read_temperature()))+" Deg")

        #Voltage Info Box
        self.voltLabelVariableHand = Tkinter.StringVar()
        voltLabelHand = Tkinter.Label(self,textvariable=self.voltLabelVariableHand,
                              anchor="w",fg="white",bg="orange")
        voltLabelHand.grid(column=0,row=4,columnspan=2,sticky='EW')
        self.voltLabelVariableHand.set(u"Voltage: "+str(int(grasperServ.read_voltage()))+" V")

        #Proportional Info Box
        self.propLabelVariableHand = Tkinter.StringVar()
        propLabelHand = Tkinter.Label(self,textvariable=self.propLabelVariableHand,
                              anchor="w",fg="white",bg="blue")
        propLabelHand.grid(column=0,row=5,columnspan=2,sticky='EW')
        self.propLabelVariableHand.set(u"Proportional Gain: "+str(int(grasperServ.read_propGain()))+" Units")

        #Derivative Info Box
        self.dervLabelVariableHand = Tkinter.StringVar()
        dervLabelHand = Tkinter.Label(self,textvariable=self.dervLabelVariableHand,
                              anchor="w",fg="white",bg="red")
        dervLabelHand.grid(column=0,row=6,columnspan=2,sticky='EW')
        self.dervLabelVariableHand.set(u"Derivative Gain: "+str(int(grasperServ.read_dervGain()))+" Units")

        #Integral Info Box
        self.integLabelVariableHand = Tkinter.StringVar()
        integLabelHand = Tkinter.Label(self,textvariable=self.integLabelVariableHand,
                              anchor="w",fg="white",bg="purple")
        integLabelHand.grid(column=0,row=7,columnspan=2,sticky='EW')
        self.integLabelVariableHand.set(u"Integral Gain: "+str(int(grasperServ.read_intGain()))+" Units")

    def initializeWrist(self):
        #Angle Entry Box
        self.angleEntryVariableWrist = Tkinter.StringVar()
        self.angleEntryWrist = Tkinter.Entry(self,
            textvariable=self.angleEntryVariableWrist)
        self.angleEntryWrist.grid(column=3,row=0,sticky='EW')
        self.angleEntryWrist.bind("<Return>", self.Wrist_OnPressEnter_Angle)
        self.angleEntryVariableWrist.set(u"Enter Angle Here")

        #Angle Entry Button
        angleEnterButtonWrist = Tkinter.Button(self,text=u"Enter",
            command=self.Wrist_OnPressButton_Angle)
        angleEnterButtonWrist.grid(column=4,row=0)

        #Angle Info Box
        self.angleLabelVariableWrist = Tkinter.StringVar()
        angleLabelWrist = Tkinter.Label(self,textvariable=self.angleLabelVariableWrist,
                              anchor="w",fg="white",bg="blue")
        angleLabelWrist.grid(column=3,row=1,columnspan=2,sticky='EW')
        self.angleLabelVariableWrist.set(u"Angle: "+str(round(float(math.degrees(wristServ.read_angle())),2))+" Deg")

        #Load Info Box
        self.loadLabelVariableWrist = Tkinter.StringVar()
        loadLabelWrist = Tkinter.Label(self,textvariable=self.loadLabelVariableWrist,
                              anchor="w",fg="white",bg="red")
        loadLabelWrist.grid(column=3,row=2,columnspan=2,sticky='EW')
        self.loadLabelVariableWrist.set(u"Load: "+str(int(wristServ.read_load()))+" Units")

        #Temp Info Box
        self.tempLabelVariableWrist = Tkinter.StringVar()
        tempLabelWrist = Tkinter.Label(self,textvariable=self.tempLabelVariableWrist,
                              anchor="w",fg="white",bg="purple")
        tempLabelWrist.grid(column=3,row=3,columnspan=2,sticky='EW')
        self.tempLabelVariableWrist.set(u"Temp: "+str(int(wristServ.read_temperature()))+" Deg")

        #Voltage Info Box
        self.voltLabelVariableWrist = Tkinter.StringVar()
        voltLabelWrist = Tkinter.Label(self,textvariable=self.voltLabelVariableWrist,
                              anchor="w",fg="white",bg="orange")
        voltLabelWrist.grid(column=3,row=4,columnspan=2,sticky='EW')
        self.voltLabelVariableWrist.set(u"Voltage: "+str(int(wristServ.read_voltage()))+" V")

        #Proportional Info Box
        self.propLabelVariableWrist = Tkinter.StringVar()
        propLabelWrist = Tkinter.Label(self,textvariable=self.propLabelVariableWrist,
                              anchor="w",fg="white",bg="blue")
        propLabelWrist.grid(column=3,row=5,columnspan=2,sticky='EW')
        self.propLabelVariableWrist.set(u"Proportional Gain: "+str(int(wristServ.read_propGain()))+" Units")

        #Derivative Info Box
        self.dervLabelVariableWrist = Tkinter.StringVar()
        dervLabelWrist = Tkinter.Label(self,textvariable=self.dervLabelVariableWrist,
                              anchor="w",fg="white",bg="red")
        dervLabelWrist.grid(column=3,row=6,columnspan=2,sticky='EW')
        self.dervLabelVariableWrist.set(u"Derivative Gain: "+str(int(wristServ.read_dervGain()))+" Units")

        #Integral Info Box
        self.integLabelVariableWrist = Tkinter.StringVar()
        integLabelWrist = Tkinter.Label(self,textvariable=self.integLabelVariableWrist,
                              anchor="w",fg="white",bg="purple")
        integLabelWrist.grid(column=3,row=7,columnspan=2,sticky='EW')
        self.integLabelVariableWrist.set(u"Integral Gain: "+str(int(wristServ.read_intGain()))+" Units")

    def Hand_OnPressButton_Angle(self):
        grasperServ.move_angle(math.radians(float(self.angleEntryVariableHand.get())))
        self.UpdateValsHand()
        self.angleEntryHand.focus_set()
        self.angleEntryHand.selection_range(0, Tkinter.END)
    
    # Open SPI bus
    spi = spidev.SpiDev()
    spi.open(0,0)
     
    # Function to read SPI data from MCP3008 chip
    # Channel must be an integer 0-7
    def ReadChannel(channel):
      adc = spi.xfer2([1,(8+channel)<<4,0])
      data = ((adc[1]&3) << 8) + adc[2]
      return data
 
    # Define sensor channels
    # (channels 3 to 7 unused)
    swt_channel = 0
    vrx_channel = 1
    vry_channel = 2
     
    # Define delay between readings (s)
    delay = 0.5
    
    def Hand_OnJoyStick_Angle(self):
        #get analog input value (voltage) and convert to angle
        vrx_pos = ReadChannel(vrx_channel)
        movespeed = float(vrx_pos/1023.0)*5.0
        old_angle = float(math.degrees(grasperServ.read_angle()))
        new_angle = old_angle + movespeed
        grasperServ.move_angle(math.radians(new_angle))
        self.UpdateValsHand()
        self.angleEntryHand.focus_set()
        self.angleEntryHand.selection_range(0, Tkinter.END)

    def Hand_OnPressEnter_Angle(self, event):
        self.Hand_OnPressButton_Angle()

    def UpdateValsHand(self): #make this a thread and update continuously
        self.angleLabelVariableHand.set(u"Angle: "+str(round(float(math.degrees(grasperServ.read_angle())),2))+" Deg")
        self.loadLabelVariableHand.set(u"Load: "+str(int(grasperServ.read_load()))+" Units")
        self.tempLabelVariableHand.set(u"Temp: "+str(int(grasperServ.read_temperature()))+" Deg")
        self.voltLabelVariableHand.set(u"Voltage: "+str(int(grasperServ.read_voltage()))+" V")

    def Wrist_OnPressButton_Angle(self):
        wristServ.move_angle(math.radians(float(self.angleEntryVariableWrist.get())))
        self.UpdateValsWrist()
        self.angleEntryWrist.focus_set()
        self.angleEntryWrist.selection_range(0, Tkinter.END)

    def Wrist_OnPressEnter_Angle(self, event):
        self.Wrist_OnPressButton_Angle()

    def UpdateValsWrist(self): #make this a thread and update continuously
        self.angleLabelVariableWrist.set(u"Angle: "+str(round(float(math.degrees(wristServ.read_angle())),2))+" Deg")
        self.loadLabelVariableWrist.set(u"Load: "+str(int(wristServ.read_load()))+" Units")
        self.tempLabelVariableWrist.set(u"Temp: "+str(int(wristServ.read_temperature()))+" Deg")
        self.voltLabelVariableWrist.set(u"Voltage: "+str(int(wristServ.read_voltage()))+" V")

    def initializeServo(self):
        global dyn
        global grasperServ
        global wristServ

        dyn = USB2Dynamixel_Device('/dev/ttyUSB0', 1000000)
        grasperServ = Robotis_Servo( dyn, 1, "AX")
        wristServ = Robotis_Servo( dyn, 2, "AX")

#class updateVals (threading.Thread):
#    def __init__(self, delay, servo):
#        threading.Thread.__init__(self)
#        while True:
#            time.sleep(delay)
#            if servo == 1:
#                gui.UpdateValsHand()
#            elif servo == 2:
#                gui.UpdateValsWrist()


if __name__ == "__main__":

    global gui
    gui = controlPanelGUI(None)
    ## Create new threads
    #HandThread = updateVals(2,1)
    #WristThread = updateVals(2,2)

    #gui.HandThread.start()
#    gui.WristThread.start()
    gui.title('Servo Control')
    gui.mainloop()



