import time
from machine import Pin, I2C,Timer
import math
from code_sensor_micro import kleurSensorDriver
from pwm_i2c import PCA9685
from auto_bewegen2 import CarDriver, MotorDriver
from wifi import connect_wifi
from mqtt import connect_mqtt, publish_meeting
from umqtt_simple import MQTTClient
from besturing_stoel2 import car2_control

teller = 0
stoel2 = CarDriver()
ks = kleurSensorDriver()
stl2 = car2_control()

# wifi
wifi_ssid = "Eindwerk_Senne"
wifi_password = "CoppensTest123"

# mqtt
mqtt_client_id = "zetel2"
mqtt_server = "192.168.1.104"
mqtt_port = 1883
mqtt_topic = "quiz"
drukKnop = False

def sub_cb(topic, msg):
   # print("test")
    if(msg == b'R3S12'):
        stl2.round_3_seat_12()
    if(msg == b'STOP'):
        stoel2.CarStop()
        print("stop")
    if(msg == b'RESET'):
        print("reset")
        stl2.round_reset()
            
def main():   
    connect_wifi(wifi_ssid,wifi_password)
    client = MQTTClient(mqtt_client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(mqtt_topic)
 
    while True:      
        stl2.msgRound(stl2.readMessage(client))
        
main()
