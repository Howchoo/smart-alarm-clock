#!/usr/bin/env python


import i2c_driver
import time


mylcd = i2c_driver.LCD()


while True:
    mylcd.lcd_display_string(time.strftime('%I:%M:%S %p'), 1)
    mylcd.lcd_display_string(time.strftime('%a %b %d, 20%y'), 2)
