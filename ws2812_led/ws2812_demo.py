from ws2812 import ws2812_led
from time import sleep_ms


#initialize the WS2812 RGB LED
print("Initializing LED")
led = ws2812_led()
#set the LED to white at boot
led.setrgb((255,255,255))
sleep_ms(1000)
led.setrgb((0,255,255))
