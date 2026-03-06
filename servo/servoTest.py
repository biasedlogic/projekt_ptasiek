from servo import Servo
from machine import Pin
from time import sleep_ms
        
servo = Servo(Pin(29))

duty = 500
while True:
    sleep_ms(100)
    servo.duty_us(duty)
    
    duty+=10
    if duty>2500: duty = 500