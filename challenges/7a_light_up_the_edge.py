"""
Light Up the Edge - A

Write a function that will turn on or off the pixels (LEDs) along one edge
(left, right, top, bottom)

Inputs:
string: side
"""

from microbit import *


def on_edge(side):
    display.clear()

    if side == "up":
        display.set_pixel(0, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(2, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(4, 0, 9)
    elif side == "down":
        display.set_pixel(0, 4, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(2, 4, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(4, 4, 9)
    elif side == "left":
        display.set_pixel(0, 0, 9)
        display.set_pixel(0, 1, 9)
        display.set_pixel(0, 2, 9)
        display.set_pixel(0, 3, 9)
        display.set_pixel(0, 4, 9)
    elif side == "right":
        display.set_pixel(4, 0, 9)
        display.set_pixel(4, 1, 9)
        display.set_pixel(4, 2, 9)
        display.set_pixel(4, 3, 9)
        display.set_pixel(4, 4, 9)


on_edge("up")
sleep(1000)
on_edge("right")
sleep(1000)
on_edge("down")
sleep(1000)
on_edge("left")
sleep(1000)
