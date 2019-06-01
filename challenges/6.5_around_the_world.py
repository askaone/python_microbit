"""
Around the World

Write a function that turns on then off 1 pixel at a time, going around the edge

Inputs:
string: direction (left or right)
Tuple: start_position (and x, y pair)

Extra Challange:
* Validate the start position and make sure it is along the edge
* Use the buttons for change the direction
"""

from microbit import *

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"


def clear_turn_on_led(x, y):
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(500)


def clear_turn_on(direction, x, y):
    if direction == RIGHT:
        x += 1
    elif direction == LEFT:
        x -= 1
    elif direction == DOWN:
        y += 1
    elif direction == UP:
        y -= 1

    clear_turn_on_led(x, y)

    return x, y


def validate_coor(direction, x, y):
    directions = None
    if direction == RIGHT:
        if x == 0 and 0 < y <= 4:
            directions = UP
        elif x == 4 and 0 <= y < 4:
            directions = DOWN
        elif y == 0 and 0 <= x < 4:
            directions = RIGHT
        elif y == 4 and 0 < x <= 4:
            directions = LEFT
        else:
            raise ValueError("Bad Coordinates")
    else:
        if x == 0 and 0 <= y < 4:
            directions = DOWN
        elif x == 4 and 0 < y <= 4:
            directions = UP
        elif y == 0 and 0 < x <= 4:
            directions = LEFT
        elif y == 4 and 0 <= x < 4:
            directions = RIGHT
        else:
            raise ValueError("Bad Coordinates")

    return directions


def around_the_world(direction, start_position):
    x = start_position[0]
    y = start_position[1]

    while True:
        directions = validate_coor(direction, x, y)

        x, y = clear_turn_on(directions, x, y)

        if button_a.is_pressed():
            direction = LEFT
            directions = validate_coor(direction, x, y)
        if button_b.is_pressed():
            direction = RIGHT
            directions = validate_coor(direction, x, y)


around_the_world(LEFT, (0, 0))
