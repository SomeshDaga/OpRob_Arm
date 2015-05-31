import Tkinter
from Servo import *
import math

class HandGui:

    def initializeHandGui(self):

        #Angle Entry Box
        self.angleEntryVariableHand = Tkinter.StringVar()
        self.angleEntryHand = Tkinter.Entry(self,
            textvariable=self.angleEntryVariableHand)
        self.angleEntryHand.grid(column=0,row=0,sticky='EW')
        self.angleEntryHand.bind("<Return>", self.Hand_OnPressEnter_Angle)
        self.angleEntryVariableHand.set(u"Enter Angle Here")    

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

    def Hand_OnPressButton_Angle(self):
        grasperServ.move_angle(math.radians(float(self.angleEntryVariableHand.get())))
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