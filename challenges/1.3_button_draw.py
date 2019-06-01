"""
Pressing Draw

Drawing when you press a button
"""

# Basic library for interact with Micro:bit device
from microbit import *


# Run forever
while True:
    # Get True if the button A is pressed
    if button_a.is_pressed():
        # Draw a heart
        display.show(Image.HEART)
    # Get True if the button B is pressed
    elif button_b.is_pressed():
        # Draw a happy face
        display.show(Image.HAPPY)
