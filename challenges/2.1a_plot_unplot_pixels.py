"""
Plot / Unplot Pixels 1-A

Turn on the first (at 0, 0) pixel or led using the creation of an Image
"""

# Basic library for interact with Micro:bit device
from microbit import *

# Create a simple image with only the first LED on
image = Image("90000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
# Display the created image on the screen
display.show(image)

# Wait 2 seconds
sleep(2000)

# Create a new image with all the LEDs off
image = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
# Display the new image on the screen
display.show(image)
