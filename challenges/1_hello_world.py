"""
Hello World

Simple project for display text and image on the screen
"""

# Basic library for interact with Micro:bit device
from microbit import *


# Run forever
while True:
    # Scroll the string on the screen
    display.scroll('Hello, World!')

    # Draw in the screen a "heart" image
    display.show(Image.HEART)

    # Wait for two seconds (2000 miliseconds)
    sleep(2000)
