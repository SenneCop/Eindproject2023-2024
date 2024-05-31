import machine
import time
from machine import Pin

class kleurSensorDriver():
    def meetKleur(self):
        sen_S0 = machine.Pin(14, machine.Pin.OUT)
        sen_S1 = machine.Pin(15, machine.Pin.OUT)
        sen_S2 = machine.Pin(17, machine.Pin.OUT)
        sen_S3 = machine.Pin(16, machine.Pin.OUT)
        sen_OUT = machine.time_pulse_us(18,1,1000000)

        teller = 0
        tellerNone = 0
        tellerRed = 0
        tellerGreen = 0
        tellerBlue = 0
        color = "NONE"
        prev_color = "NONE"
        colorArray=["","",""]

        # Set output frequency scaling to 20%
        sen_S0.on()
        sen_S1.off()
        
        #kleur meten
        while(teller != 10):
            kleur = [0,0,0]
            #kleur = [R,G,B]
    
            sen_S2.off()
            sen_S3.off()
            time.sleep(0.01)   
            red_freq = machine.time_pulse_us(18,1,1000000)		#RED
    

            sen_S2.on()
            sen_S3.on()
            time.sleep(0.01)
            green_freq = machine.time_pulse_us(18,1,1000000)	#GREEN
        
        
            sen_S2.off()
            sen_S3.on()
            time.sleep(0.01)
            blue_freq = machine.time_pulse_us(18,1,1000000)		#BLUE
        
           
            kleur = [red_freq,green_freq,blue_freq]
            colorArray = kleur
            # colorArray[R,G,B]
            # colorArray[0,1,2]
            
            if colorArray[0] > 400 or colorArray[1] > 400 or colorArray[2] > 400:
                color = "NONE"
            elif colorArray[0] < colorArray[1] and  colorArray[0] < colorArray[2]:
                color = "RED"
            elif colorArray[1] < colorArray[0] and  colorArray[1] < colorArray[2]:
                color = "GREEN"
            elif colorArray[2] < colorArray[1] and  colorArray[2] < colorArray[0]:
                color = "BLUE"

            colorList = ["","","","","","","","","","","","","","","","","","","",""]
            colorList[teller] = color
            teller = teller + 1 
       
    
            if teller == 10:
                teller = 0
                for color in colorList:
                    if color is "NONE":
                        tellerNone = tellerNone + 1      
                    elif color=="RED":
                        tellerRed = tellerRed + 1
                    elif color=="GREEN":
                        tellerGreen = tellerGreen + 1 
                    elif color =="BLUE":
                        tellerBlue = tellerBlue + 1
                
                if tellerNone > tellerRed and tellerNone > tellerGreen and tellerNone > tellerBlue:
                    trueColor = "NONE"
                if tellerRed > tellerNone and tellerRed > tellerGreen and tellerRed > tellerBlue:
                    trueColor = "RED"
                if tellerGreen > tellerRed and tellerGreen > tellerNone and tellerGreen > tellerBlue:
                    trueColor = "GREEN"
                if tellerBlue > tellerRed and tellerBlue > tellerGreen and tellerBlue > tellerNone:
                    trueColor = "BLUE"
            
                tellerNone = 0
                tellerRed = 0
                tellerGreen = 0
                tellerBlue = 0
                colorList.clear()
                return  trueColor
    

    