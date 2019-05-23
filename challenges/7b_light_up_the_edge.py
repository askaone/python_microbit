"""
Light Up the Edge - B

Write a function that will turn on or off the pixels (LEDs) along one edge
(left, right, top, bottom)

Inputs:
string: side
"""

from microbit import *


def on_edge(side):
    display.clear()

    for n in range(0, 5):
        if side == "up":
            display.set_pixel(n, 0, 9)
        elif side == "down":
            display.set_pixel(n, 4, 9)
        elif side == "left":
            display.set_pixel(0, n, 9)
        elif side == "right":
            display.set_pixel(4, n, 9)


on_edge("up")
sleep(1000)
on_edge("right")
sleep(1000)
on_edge("down")
sleep(1000)
on_edge("left")
sleep(1000)
