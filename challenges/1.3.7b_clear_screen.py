"""
Clear Screen

Simple turn off all the LEDs using the API for manipulate the screen
"""

# Basic library for interact with Micro:bit device
from microbit import *

# Show the HAPPY face is only for show the LEDs shutdown
display.show(Image.HAPPY)

# Wait 2 seconds
sleep(2000)

# This function turn off all LEDs
display.clear()
