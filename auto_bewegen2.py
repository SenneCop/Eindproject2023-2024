import time
from machine import Pin, I2C
import math
from pwm_i2c import PCA9685


class MotorDriver():
    def __init__(self, debug=False):
        self.debug = debug
        self.pwm = PCA9685()
        self.pwm.setPWMFreq(50)       
        self.MotorPin = ['MA', 0,1,2, 'MB',3,4,5, 'MC',6,7,8, 'MD',9,10,11]
        self.MotorDir = ['backward', 0,1, 'forward',1,0]

    def MotorRun(self, motor, mdir, speed):
        if speed > 100:
            return
        
        mPin = self.MotorPin.index(motor)
        mDir = self.MotorDir.index(mdir)
        
        if (self.debug):
            print("set PWM PIN %d, speed %d" %(self.MotorPin[mPin+1], speed))
            print("set pin A %d , dir %d" %(self.MotorPin[mPin+2], self.MotorDir[mDir+1]))
            print("set pin b %d , dir %d" %(self.MotorPin[mPin+3], self.MotorDir[mDir+2]))

        self.pwm.setServoPulse(self.MotorPin[mPin+1], speed)        
        self.pwm.setLevel(self.MotorPin[mPin+2], self.MotorDir[mDir+1])
        self.pwm.setLevel(self.MotorPin[mPin+3], self.MotorDir[mDir+2])
        
        
       # self.pwm.setServoPulse(self.MotorPin[mPin+1], 0)
       # self.pwm.setLevel(self.MotorPin[mPin+2], 0)
       # self.pwm.setLevel(self.MotorPin[mPin+3], 0)

    def MotorStop(self, motor):
        mPin = self.MotorPin.index(motor)
        self.pwm.setServoPulse(self.MotorPin[mPin+1], 0)
        
   
   
class CarDriver():    
    def CarForward(self, debug=False):
         m= MotorDriver()
         m.MotorRun('MA', 'forward', 65)
         m.MotorRun('MB', 'forward', 65)
         m.MotorRun('MC', 'backward', 65)
         m.MotorRun('MD', 'backward', 65)
                 
    def CarBackward(self, debug=False):
         m= MotorDriver()
         m.MotorRun('MA', 'backward', 65)
         m.MotorRun('MB', 'backward', 65)
         m.MotorRun('MC', 'forward', 65)
         m.MotorRun('MD', 'forward', 65)
            
    def CarLeft(self, debug=False):
         m= MotorDriver()
         m.MotorRun('MA', 'forward', 65)
         m.MotorRun('MB', 'backward', 65)
         m.MotorRun('MC', 'backward', 65)
         m.MotorRun('MD', 'forward', 65)
         
        
    def CarRight(self, debug=False):
         m= MotorDriver()
         m.MotorRun('MA', 'backward', 65)
         m.MotorRun('MB', 'forward', 65)
         m.MotorRun('MC', 'forward', 65)
         m.MotorRun('MD', 'backward', 65)
         
    def CarStop(self, debug=False):
         m= MotorDriver()
         m.MotorStop('MA')
         m.MotorStop('MB')
         m.MotorStop('MC')
         m.MotorStop('MD')
         

