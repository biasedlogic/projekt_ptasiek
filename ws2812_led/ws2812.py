from machine import Pin
import rp2


class ws2812_led():
    def __init__(self,pin=16):
        self.max_lum =100
        self.r=0
        self.g=0
        self.b=0
        self.sm = rp2.StateMachine(0, self.ws2812, freq=8_000_000, sideset_base=Pin(pin))
        self.sm.active(1)

    @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
    def ws2812():
        T1 = 2
        T2 = 5
        T3 = 3
        wrap_target()
        label("bitloop")
        out(x, 1)               .side(0)    [T3 - 1]
        jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
        jmp("bitloop")          .side(1)    [T2 - 1]
        label("do_zero")
        nop()                   .side(0)    [T2 - 1]
        wrap()

#     def setrgb(self,r,g,b):
#         self.r=r
#         self.g=g
#         self.b=b
#         rgb =(g<<24) | (r<<16) | (b<<8)
#         self.sm.put(rgb)
        
    def setrgb(self,rgb):
        self.r=rgb[0]
        self.g=rgb[1]
        self.b=rgb[2]
        rgb =(self.g<<24) | (self.r<<16) | (self.b<<8)
        self.sm.put(rgb)