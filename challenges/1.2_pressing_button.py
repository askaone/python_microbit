"""
Pressing Button

Simple project for exercise the capture the event of press a button
"""

# Basic library for interact with Micro:bit device
from microbit import *


# Wait for ten seconds
sleep(10000)

# Get the total times the button "A" has been pressed
display.scroll(str(button_a.get_presses()))
