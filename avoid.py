#!/usr/bin/env python
# This code had been modified by: Ian Catapano
# Modifications made for Pi Rover Project

from rrb3 import *
import time, random

# Set the batter and motor voltage, motor voltage effects speed
rr = RRB3(9.0, 3.0)

# This value should be set to False if you are using a switch
# I am not using a switch, the rover starts when I start the program
running = True

# Select the direction to turn at random when an object is detected
def turn_randomly():
    turn_time = random.randint(1, 3)
    if random.randint(1, 2) == 1:
        rr.left(turn_time, 0.5) # turn at half speed
    else:
        rr.right(turn_time, 0.5)
    rr.stop()

# Check for objects less than 50 cms infromt of rover
try:
    while True:
        distance = rr.get_distance()
        print(distance)
        if distance < 50 and running:
            turn_randomly()
        if running:
            rr.forward(0)
        if rr.sw2_closed():
            running = not running
        if not running:
            rr.stop()
        time.sleep(0.2)

# Close out program
finally:
    print("Exiting")
    rr.cleanup()
    
