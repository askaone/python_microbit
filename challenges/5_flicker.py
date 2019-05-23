"""
Flicker: On / Off Multiple Times

Write a function that will turn a pixel (LED) on and off a certain number of
times. Start by clearing out the LED display (turn off all the pixels (LEDs))

Inputs:
int: X position
int: Y position
int: flicker_count, number of time to turn the LED on and off
"""

# Basic library for interact with Micro:bit device
from microbit import *


# ... Read at the top of this file -.-
def flicker(x, y, times):
    # Loop for iterate turning on and off the LED
    for n in range(1, times + 1):
        # Clear the screen
        display.clear()
        # Wait 1 second
        sleep(1000)
        # Turn on the LED (X, Y)
        display.set_pixel(x, y, 9)
        # Wait 1 second
        sleep(1000)

    # Clear the screen at the END
    display.clear()

# Call our function
flicker(3, 4, 5)
