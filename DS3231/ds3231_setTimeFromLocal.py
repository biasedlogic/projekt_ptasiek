from machine import RTC,I2C
from ds3231_gen import DS3231
from time import localtime

# Remember to allow Thonny to set the RTC on connect for this to work!

print("local time:",localtime())
i2c = I2C()
sys_rtc = RTC()
ext_rtc = DS3231(i2c)
print("ext rtc time",ext_rtc.get_time())
ext_rtc.set_time(localtime())
print("setting ext_rtc")
print("local time:",localtime())
print("ext rtc time",ext_rtc.get_time())