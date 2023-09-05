from pyautogui import *
from time import sleep
import sys
import webbrowser as wb

def paint(x, y):
    sleep(2)
    screen_width, screen_height = size()
    print("Screen Width & Height:", screen_width, screen_height)
    currentMouseX, currentMouseY = position()
    print("currentMouse X, Y:", currentMouseX, currentMouseY)

    moveTo(x , y)
    distance = 200
    while distance > 0:
        # moves the cursor to the right
        dragRel(distance, 0, duration=0.1, button='left')
        distance = distance - 15
        print("currentMouse X, Y:", currentMouseX, currentMouseY)

        moveTo(x, y)
        distance = 200
        while distance > 0:
            # moves the cursor to the right
            dragRel(distance, 0, duration=0.1, button='left')
            distance = distance - 15
            # move the cursor down

        # move the cursor down
        dragRel(0, distance, duration=0.1,button='left')
        # move the cursor to the left
        dragRel(-distance, 0, duration=0.1,button='left')
        distance = distance - 15
        # move the cursor up
        dragRel(0, -distance, duration=0.1,button='left')


paint(500,400)

paint(900,400)