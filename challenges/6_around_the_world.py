"""
Around the World

Write a function that turns on then off 1 pixel at a time, going around the edge

Inputs:
string: direction (left or right)
Tuple: start_position (and x, y pair)

Extra Challange:
* Validate the start position and make sure it is along the edge
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
            raise ValueError("Bad Coordinates")
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
        else:
            raise ValueError("Bad Coordinates")

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
