import time
from machine import Pin, I2C,Timer
import math
from code_sensor_micro import kleurSensorDriver
from pwm_i2c import PCA9685
from auto_bewegen2 import CarDriver, MotorDriver
from wifi import connect_wifi
from mqtt import connect_mqtt, publish_meeting
from umqtt_simple import MQTTClient

teller = 0
stoel2 = CarDriver()
ks = kleurSensorDriver()

# wifi
wifi_ssid = "Eindwerk_Senne"
wifi_password = "CoppensTest123"

# mqtt
mqtt_client_id = "zetel2"
mqtt_server = "192.168.1.104"
mqtt_port = 1883
mqtt_topic = "quiz"

class car2_control():
    
    def readMessage(self,client):
        msg = client.check_msg()   
        return msg
    
    def msgRound(self,msg):       
        if(msg == b'R3S12'):
            round_3_seat_12()
        if(msg == b'STOP'):
            stoel1.CarStop()
            print("stop")
        if(msg == b'RESET'):
            print("reset")
            round_reset()
    
    def round_3_seat_12(self):
        drukKnop = False
        startTimeSeconds = time.time()
        stoel2.CarStop()
        color = ks.meetKleur()
        pastTimeSeconds = time.time()-startTimeSeconds
        #print("ziet stop kleur")
    
       
        while(color != "RED" or pastTimeSeconds < 2):
            stoel2.CarForward()
            color = ks.meetKleur()
            pastTimeSeconds = time.time()-startTimeSeconds
            print(f"color: {color} time: {pastTimeSeconds} voorwaarts")
            
        startTimeSeconds = time.time()
        while(color != "GREEN" or pastTimeSeconds < 2):
            stoel2.CarRight()
            color = ks.meetKleur()
            pastTimeSeconds = time.time()-startTimeSeconds
            print(f"color: {color} time: {pastTimeSeconds} rechts")
        stoel2.CarStop()
    
    def round_3_seat_13(self):
        startTimeSeconds = time.time()
        stoel2.CarStop()
        color = ks.meetKleur()
        pastTimeSeconds = time.time()-startTimeSeconds
        #print("ziet stop kleur")
    
        while(color != "BLEU" or pastTimeSeconds < 2):
            stoel2.CarLeft()
            color = ks.meetKleur()
            pastTimeSeconds = time.time()-startTimeSeconds
            #print(f"color: {color} time: {pastTimeSeconds} voorwaarts")
            
        startTimeSeconds = time.time()    
        while(color != "BLUE" or pastTimeSeconds < 2):
            stoel2.CarForward()
            color = ks.meetKleur()
            pastTimeSeconds = time.time()-startTimeSeconds
            #print(f"color: {color} time: {pastTimeSeconds} voorwaarts")
            
        startTimeSeconds = time.time()
        while(color != "RED" or pastTimeSeconds < 2):
            stoel2.CarRight()
            color = ks.meetKleur()
            pastTimeSeconds = time.time()-startTimeSeconds
            #print(f"color: {color} time: {pastTimeSeconds} rechts")
        stoel1.CarStop()
        
        
        
    def round_3_seat_14(self):
        startTimeSeconds = time.time()
        stoel2.CarStop()
        color = ks.meetKleur()
        pastTimeSeconds = time.time()-startTimeSeconds
        #print("ziet stop kleur")
    
        while(color != "BLEU" or pastTimeSeconds < 2):
            stoel2.CarLeft()
            color = ks.meetKleur()
            pastTimeSeconds = time.time()-startTimeSeconds
            #print(f"color: {color} time: {pastTimeSeconds} voorwaarts")
            
        startTimeSeconds = time.time()    
        while(color != "BLUE" or pastTimeSeconds < 2):
            stoel2.CarForward()
            color = ks.meetKleur()
            pastTimeSeconds = time.time()-startTimeSeconds
            #print(f"color: {color} time: {pastTimeSeconds} voorwaarts")
            
        startTimeSeconds = time.time()
        while(color != "RED" or pastTimeSeconds < 2):
            stoel2.CarRight()
            color = ks.meetKleur()
            pastTimeSeconds = time.time()-startTimeSeconds
            #print(f"color: {color} time: {pastTimeSeconds} rechts")
        stoel1.CarStop()
        
        
        
    def round_reset(self):
        resetColors = ["",""]
        color = ks.meetKleur()
        
        while(color == "NONE"):
            stoel2.CarLeft()
            color = ks.meetKleur()
        stoel2.CarStop()
        resetColors[0] = color
        
        while(color == "NONE"):
            stoel2.CarBackward()
            color = ks.meetKleur()
        stoel2.CarStop()
        color = ks.meetKleur()
        resetColors[1] = color


