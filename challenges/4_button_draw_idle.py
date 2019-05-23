"""
Pressing Draw Idle

Drawing when you press a button, and reset when idle
"""

# Basic library for interact with Micro:bit device
from microbit import *


# Variable for control the time
timer = 0


# Run forever
while True:
    # Get True if the button A is pressed
    if button_a.is_pressed():
        # Draw a heart
        display.show(Image.HEART)
        timer = 0
    # Get True if the button B is pressed
    elif button_b.is_pressed():
        # Draw a happy face
        display.show(Image.HAPPY)
        timer = 0

    timer += 1
    if timer > 1000:
        display.show(Image.SAD)
