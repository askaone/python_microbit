# Python Micro:bit Challenges

This is a collection of challenges for solve in python with the Micro:bit device.

## Hello World

In this chapter you will learn the basics instruction to program the Micro:bit with Python. We will show you the functions from the API that you will need for be able to solve this challenges.

### First Step... Say Hello

For work with the Micro:bit on Python you need import the libraries and resources required by the device.

```python
from microbit import *
```

Now, you can call the **scroll** function to show in the screen the message *Hello World*.

```python
display.scroll('Hello, World!')
```

Also, you can draw an Image by your own or a pre-made.

```python
# Draw in the screen a "heart" image
display.show(Image.HEART)
```

And, if you want *wait* between instruction you have the **sleep** function, this receive as a parameter how long has to wait in milliseconds.

```python
sleep(1000)
```

> You will found an example [here](1_hello_world.py)

### Pressing Button

Maybe you will want also press the buttons on the device.

## Plot / Unplot Pixels

## Flicker: On / Off Multiple Times

## Random Plotting

## Light Up the Edge

## Around the World

## Pixel Rain

## Pixel Control

## Pixel Collision
