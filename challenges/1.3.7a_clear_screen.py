"""
Clear Screen

Simple turn off all the LEDs using the creation of an Image
"""

# Basic library for interact with Micro:bit device
from microbit import *

# Show the HAPPY face is only for show the LEDs shutdown
display.show(Image.HAPPY)

# Wait 2 seconds
sleep(2000)

# Create an image with all the LEDs off
image = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
# Display the image on the screen
display.show(image)
