from machine import PWM

class Servo():
    
    def __init__(self,pin,initppm=1500):
        self.__PWM__ = PWM(pin,freq=50)
        self.ppm = initppm
        self.update()
        
    def update(self):
        ducy_u16 = int(65536*self.ppm/20000)
        self.__PWM__.duty_u16(ducy_u16)
        
    def duty_us(self,ppm):
        self.ppm = ppm
        self.update()