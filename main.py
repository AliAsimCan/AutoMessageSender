import pyautogui
import time

def mesaj():
    pyautogui.write("I'm trying to python code.")
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(0.5)
