"""
Plot / Unplot Pixels 2

Figure out the X, Y coordinate system for the Micro:bit
a. Where is the origin
b. What are the min/max values for X and Y
"""

# Basic library for interact with Micro:bit device
from microbit import *


# Turn on the first LED on (0, 0) (X, Y).
# This is the origin, also is the min value posible for X and Y.
display.set_pixel(0, 0, 9)
# Turn on the last LED on (4, 4) (X, Y).
# This is the end of the screen, also is the max value for X and Y
display.set_pixel(4, 4, 9)

# Wait 2 seconds
sleep(2000)

# Turn off the LED (0, 0)
display.set_pixel(0, 0, 0)
# Turn off the LED (4, 4)
display.set_pixel(4, 4, 0)
