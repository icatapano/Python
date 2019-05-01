#!/usr/bin/env python
# This code had been modified by: Ian Catapano
# Modifications made for Pi Rover Project

# Use the arrow keys to direct the robot

from rrb3 import *
import sys
import tty
import termios

# Set the batter and motor voltage, motor voltage effects speed
rr = RRB3(9.0, 3.0) 

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

print("Use the arrow keys to move the robot")
print("Press CTRL-C to quit the program")

# Read in keyboard input, meant to capture arrow keys and interrupt
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

# Deteremine which arrow key was pressed
def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

# Controls the motors based of key pressed and displays direction on the screen
try: 
    while True:
        keyp = readkey()
        if keyp == UP:
            rr.forward() # With no argument, the motor runs continiously
            print 'forward'
        elif keyp == DOWN:
            rr.reverse(1) # With an argument, motor will run for units set
            print 'backward'
        elif keyp == RIGHT:
            rr.right(1)
            print 'clockwise'
        elif keyp == LEFT:
            rr.left(1)
            print 'anti clockwise'
        elif keyp == ' ':
            rr.stop()
            print 'stop'
        elif ord(keyp) == 3:
            break

# Close out GPIO pins
except KeyboardInterrupt:
    GPIO.cleanup()

