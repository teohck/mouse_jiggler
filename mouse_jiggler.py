#  /$$      /$$                                              /$$$$$/$$                  /$$                  
# | $$$    /$$$                                             |__  $|__/                 | $$                  
# | $$$$  /$$$$ /$$$$$$ /$$   /$$ /$$$$$$$ /$$$$$$             | $$/$$ /$$$$$$  /$$$$$$| $$ /$$$$$$  /$$$$$$ 
# | $$ $$/$$ $$/$$__  $| $$  | $$/$$_____//$$__  $$            | $| $$/$$__  $$/$$__  $| $$/$$__  $$/$$__  $$
# | $$  $$$| $| $$  \ $| $$  | $|  $$$$$$| $$$$$$$$       /$$  | $| $| $$  \ $| $$  \ $| $| $$$$$$$| $$  \__/
# | $$\  $ | $| $$  | $| $$  | $$\____  $| $$_____/      | $$  | $| $| $$  | $| $$  | $| $| $$_____| $$      
# | $$ \/  | $|  $$$$$$|  $$$$$$//$$$$$$$|  $$$$$$$      |  $$$$$$| $|  $$$$$$|  $$$$$$| $|  $$$$$$| $$      
# |__/     |__/\______/ \______/|_______/ \_______/       \______/|__/\____  $$\____  $|__/\_______|__/      
#                                                                     /$$  \ $$/$$  \ $$                     
#                                                                    |  $$$$$$|  $$$$$$/                     
#                                                                     \______/ \______/                      

import pyautogui
import time

def move_mouse_square(step, travel_duration):
    # Get the current position once
    x, y = pyautogui.position()

    # Move right
    pyautogui.moveTo(x + step, y, duration=travel_duration)
    log_position()

    # Move down
    pyautogui.moveTo(x + step, y + step, duration=travel_duration)
    log_position()

    # Move left
    pyautogui.moveTo(x, y + step, duration=travel_duration)
    log_position()

    # Move up
    pyautogui.moveTo(x, y, duration=travel_duration)
    log_position()

def log_position():
    x, y = pyautogui.position()
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print('Moved at ' + str(result) + ' ('  + str(x) + ', ' + str(y) + ')')

step = 20
travel_duration = 0.2
pause_duration = 3

while True:
    move_mouse_square(step, travel_duration)
    time.sleep(pause_duration)