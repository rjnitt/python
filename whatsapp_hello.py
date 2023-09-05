from pyautogui import *
from time import sleep
import sys
import webbrowser as wb

#contact list
contacts = ["Vinay"]


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

def open_new_tab():
    hotkey('command', 't', interval=0.25)
    sleep(1)
    url = "web.whatsapp.com"
    typewrite(url)
    press('enter')
    sleep(12)

# def open_image():
#     locate('download.jpg')


def close_tab():
    hotkey('command', 'w', interval=0.25)


for name in contacts:
    try:
        open_new_tab()
    except:
        print("could not open")

    try:
        click_search_name(name)
    except:
        print("Unable to locate search bar or name")

    try:
        i = 1
        while i<5:
            message = "hello"
            message += str(i)
            click_send_message(message)
            i+=1
    except:
        print("Unable to locate message bar")

    try:
        close_tab()
    except:
        print("Unable to locate")

print('Messages sent successfully')