#pip install pyautogui
#python3 mouse.py

#press control + c to end the program

import pyautogui
import random

size = pyautogui.size()
width = size[0]
heigth = size[1]

try:
    while True:
        while(1):
            x = random.randint(0, width)
            y = random.randint(0, heigth)
            pyautogui.moveTo(x, y, duration = 1)
except KeyboardInterrupt:
    print('\ninterrupted!')