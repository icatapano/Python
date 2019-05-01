#!/usr/bin/env python
# This code had been modified by: Ian Catapano
# Modifications made for Pi Rover Project

import picamera
import pygame
import io

# Start pygame window to be used for video stream
pygame.init()
screen = pygame.display.set_mode((640,480),0)

# Start camera stream
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.crop = (0.0, 0.0, 1.0, 1.0)

x = (screen.get_width() - camera.resolution[0]) / 2
y = (screen.get_height() - camera.resolution[1]) / 2

# Buffer
rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

# Loop to keep camera stream going till window is closed
exitFlag = True
while(exitFlag):
    for event in pygame.event.get():
        if(event.type is pygame.MOUSEBUTTONDOWN or 
           event.type is pygame.QUIT):
            exitFlag = False

    stream = io.BytesIO()
    camera.capture(stream, use_video_port=True, format='rgb')
    stream.seek(0)
    stream.readinto(rgb)
    stream.close()
    img = pygame.image.frombuffer(rgb[0:
          (camera.resolution[0] * camera.resolution[1] * 3)],
           camera.resolution, 'RGB')

    screen.fill(0)
    if img:
        screen.blit(img, (x,y))

    pygame.display.update()

# Close turn camera off and close pygame
camera.close()
pygame.display.quit()
