# Random Plotting
"""
Random Plotting - A

Write a function that will turn a random pixel (LED) on and off.Start by
clearing out the LED display (turn off all the pixels (LEDs))
"""

# Basic library for interact with Micro:bit device
from microbit import *
# Python's library for get random number
import random


# ... Read at the top of this file -.-
def rand_plotting():
    # Get a random number for X between 0, 4
    x = random.randint(0, 4)
    # Get a random number for Y between 0, 4
    y = random.randint(0, 4)

    # Clear the screen
    display.clear()

    # Turn on the LED (X, Y)
    display.set_pixel(x, y, 9)


# Call our function
rand_plotting()
