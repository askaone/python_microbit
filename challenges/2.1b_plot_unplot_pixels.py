"""
Plot / Unplot Pixels 1-B

Turn on the first (at 0, 0) pixel or led using the API for manipulate the screen
"""

# Basic library for interact with Micro:bit device
from microbit import *

# Function for turn on/off a LED by coordinates X, Y and the brightness
# between 0 (off) and 9 (completly on)
display.set_pixel(0, 0, 9)

# Wait 2 seconds
sleep(2000)

# Turn of the LED
display.set_pixel(0, 0, 0)
