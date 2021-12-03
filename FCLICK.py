#FCLICK
#Filip Rokita
#www.filiprokita.com

import pyautogui
import keyboard
import win32api
import win32con
import time

startButton = input("START BUTTON: ").lower()

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def getPixelColor(x, y):
    screenshot = pyautogui.screenshot()
    color = screenshot.getpixel((x, y))
    return color

while True:
    while keyboard.is_pressed(startButton) == True:
        startPos = tuple(pyautogui.position())
        startColor = getPixelColor(startPos[0], startPos[1])
        while True:
            nowColor = getPixelColor(startPos[0], startPos[1])
            if nowColor != startColor:
                click(startPos[0], startPos[1])
                break