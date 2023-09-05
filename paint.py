from pyautogui import *
from time import sleep
import sys
import webbrowser as wb

#contact list
contacts = ["Pucchi"]


#idle for 7 seconds
sleep(7)

# method to find the search bar location
def click_search_name(name):
    x1, y1 = [211,250]
    moveTo(x1, y1)
    click()
    typewrite(name, interval=0.2)
    sleep(2)
    press('enter')

# def take_screenshot():
#     scree = screenshot()
#     scree.save("image.png")

# method to find and send message
def click_send_message(msg):
    x3, y3 = [950,750]
    moveTo(x3, y3)
    click()
    sleep(1)
    typewrite(message)
    press('enter')

def draw1():
    draw_x, draw_y = 500, 500
    draw_color = 'red'

    # Click and hold to start drawing
    mouseDown(draw_x, draw_y, button='left')

    # Move the mouse to draw
    for _ in range(100):
        moveTo(draw_x + _, draw_y)
        scroll(-10)  # Change the scroll value for line thickness
        sleep(0.05)

    # Release the mouse to stop drawing
    mouseUp(draw_x, draw_y, button='left')
def draw():
    # Define the coordinates where the drawing should start
    start_x, start_y = 500, 500

    # Simulate clicking to start drawing
    click(start_x, start_y)

    # Move the mouse to draw a line
    moveTo(start_x + 50, start_y + 50, duration=0.2)
    mouseDown()

    # Draw a line
    for _ in range(20):
        moveRel(10, 10, duration=0.2)

    # Release the mouse button to stop drawing
    mouseUp()

    # Wait a bit before the script finishes
    sleep(2)

def open_new_tab():
    hotkey('command', 'space', interval=0.25)
    sleep(1)
    url = "paintBrush"
    typewrite(url)
    press('enter')
    sleep(1)

# def open_image():
#     locate('download.jpg')


def close_tab():
    hotkey('command', '', interval=0.25)


def draw2():
    # initialising a variable distance
    distance = 200

    start_x, start_y = 500, 500

    # Simulate clicking to start drawing
    click(start_x, start_y)

    while (distance):
        # moves the cursor to the right
        dragRel(distance, 0, duration=0.2)
        distance = distance - 5
        # move the cursor down
        dragRel(0, distance, duration=0.2)
        # move the cursor to the left
        dragRel(-distance, 0, duration=0.2)
        distance = distance - 5
        # move the cursor up
        dragRel(0, -distance, duration=0.2)


for name in contacts:
    try:
        draw2()
    except:
        print("could not open")

    # try:
    #     click_search_name(name)
    # except:
    #     print("Unable to locate search bar or name")
    #
    # try:
    #     i = 1
    #     while i<5:
    #         message = "I Love You"
    #         message += str(i)
    #         click_send_message(message)
    #         i+=1
    # except:
    #     print("Unable to locate message bar")
    #
    # try:
    #     close_tab()
    # except:
    #     print("Unable to locate")

print('Messages sent successfully')