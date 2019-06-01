"""
Random Plotting - B

Write a function that will turn a random pixel (LED) on and off a certain number
of times. Start by clearing out the LED display (turn off all the pixels (LEDs))

Inputs:
int: times, number of time to turn the LED on and off
"""

# Basic library for interact with Micro:bit device
from microbit import *
# Python's library for get random number
import random


# ... Read at the top of this file -.-
def rand_plotting(times):
    # Get a random number for X between 0, 4
    x = random.randint(0, 4)
    # Get a random number for Y between 0, 4
    y = random.randint(0, 4)
    # Loop for flick and turn on/off the time given
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
rand_plotting(2)
