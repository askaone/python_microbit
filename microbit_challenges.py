# Hello World
from microbit import *


while True:
    display.scroll('Hello, World!')
    display.show(Image.HEART)
    sleep(2000)


"""
from microbit import *


sleep(10000)
display.scroll(str(button_a.get_presses()))
"""


"""
from microbit import *


while True:
    if button_a.is_pressed():
        display.show(Image.HEART)
    elif button_b.is_pressed():
        display.show(Image.HAPPY)
"""

"""
from microbit import *

timer = 0
while True:
    if button_a.is_pressed():
        display.show(Image.HEART)
        timer = 0
    elif button_b.is_pressed():
        display.show(Image.HAPPY)
        timer = 0

    timer += 1
    if timer > 1000:
        display.show(Image.SAD)
"""


# Plot / Unplot Pixels
# 1
### 1 - a
"""
from microbit import *

image = Image("90000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
display.show(image)

sleep(2000)

image = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
display.show(image)
"""

### 1 - b
"""
from microbit import *


display.set_pixel(0, 0, 9)

sleep(2000)

display.set_pixel(0, 0, 0)
"""

## 2
"""
from microbit import *


display.set_pixel(0, 0, 9)
display.set_pixel(4, 4, 9)

sleep(2000)

display.set_pixel(0, 0, 0)
display.set_pixel(4, 4, 0)
"""

# Flicker: On / Off Multiple Times
## clear the leds
### 1
"""
from microbit import *

# Show the HAPPY face is only for show the LEDs shutdown
display.show(Image.HAPPY)
sleep(2000)

image = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
display.show(image)
"""

### 2
"""
from microbit import *

# Show the HAPPY face is only for show the LEDs shutdown
display.show(Image.HAPPY)
sleep(2000)

display.clear()
"""

## Done
"""
from microbit import *


def flicker(x, y, times):
    for n in range(1, times + 1):
        display.clear()
        sleep(1000)
        display.set_pixel(x, y, 9)
        sleep(1000)

    display.clear()


flicker(3, 4, 5)
"""

# Random Plotting
"""
from microbit import *
import random


def rand_plotting(times):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    for n in range(1, times + 1):
        display.clear()
        sleep(1000)
        display.set_pixel(x, y, 9)
        sleep(1000)

    display.clear()


rand_plotting(2)
"""

# Light Up the Edge
## 1
"""
from microbit import *

# TODO: Think how to improve this code
# using variables for do it more
# simple and short
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


on_edge("right")
"""

## 2
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
"""

# Around the World
"""
from microbit import *

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"


def clear_turn_on_led(x, y):
    display.clear()
    display.set_pixel(x, y, 9)
    if (1 <= x <= 3 and (y == 0 or y == 4)) or (1 <= y <= 3 and (x == 0 or x == 4)):
        sleep(500)
    else:
        sleep(250)


def clear_turn_on_horizontal(direction, x, y):
    r = None

    if direction == RIGHT:
        r = range(x, 5)
    elif direction == LEFT:
        r = range(x, -1, -1)

    for n in r:
        clear_turn_on_led(n, y)


def clear_turn_on_vertical(direction, x, y):
    r = None

    if direction == DOWN:
        r = range(y, 5)
    elif direction == UP:
        r = range(y, -1, -1)

    for n in r:
        clear_turn_on_led(x, n)


def around_the_world(direction, start_position):
    x = start_position[0]
    y = start_position[1]

    directions = None
    coordinates = None
    if direction == RIGHT:
        coordinates = {UP:(0, 4), RIGHT:(0, 0), DOWN:(4, 0), LEFT:(4, 4)}
        if x == 0 and 0 < y <= 4:
            directions = [UP, RIGHT, DOWN, LEFT]
        elif x == 4 and 0 <= y < 4:
            directions = [DOWN, LEFT, UP, RIGHT]
        elif y == 0 and 0 <= x < 4:
            directions = [RIGHT, DOWN, LEFT, UP]
        elif y == 4 and 0 < x <= 4:
            directions = [LEFT, UP, RIGHT, DOWN]
    else:
        coordinates = {UP:(4, 4), RIGHT:(0, 4), DOWN:(0, 0), LEFT:(4, 0)}
        if x == 0 and 0 <= y <= 4:
            directions = [DOWN, RIGHT, UP, LEFT]
        elif x == 4 and 0 < y <= 4:
            directions = [UP, LEFT, DOWN, RIGHT]
        elif y == 0 and 0 < x <= 4:
            directions = [LEFT, DOWN, RIGHT, UP]
        elif y == 4 and 0 < x <= 4:
            directions = [RIGHT, UP, LEFT, DOWN]

    counter = 0
    while True:
        for sDirection in directions:
            coor = coordinates[sDirection]

            if counter == 0:
                coor = (x, y)
                counter += 1

            if sDirection == RIGHT or sDirection == LEFT:
                clear_turn_on_horizontal(sDirection, coor[0], coor[1])
            elif sDirection == UP or sDirection == DOWN:
                clear_turn_on_vertical(sDirection, coor[0], coor[1])


around_the_world(LEFT, (4, 2))
"""
