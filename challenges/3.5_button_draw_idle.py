"""
Pressing Draw Idle

Drawing when you press a button, and reset when idle
"""

# Basic library for interact with Micro:bit device
from microbit import *


# Variable for control time
timer = 0


# Run forever
while True:
    # Get True if the button A is pressed
    if button_a.is_pressed():
        # Draw a heart
        display.show(Image.HEART)
        # If you press the button the time is reset
        timer = 0
    # Get True if the button B is pressed
    elif button_b.is_pressed():
        # Draw a happy face
        display.show(Image.HAPPY)
        # If you press the button the time is reset
        timer = 0

    # Increment the time each cycle
    timer += 1
    # If the time is over 1000 (around 1 second) then show the idle image
    if timer > 1000:
        # Draw a das face
        display.show(Image.SAD)
