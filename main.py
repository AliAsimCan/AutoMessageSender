import pyautogui
import time

def mesaj():
    pyautogui.write("I'm trying to python code.") #You can edit the message here
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(0.5)
