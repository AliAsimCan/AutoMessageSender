import pyautogui
import time

def mesaj():
    pyautogui.write("hayreddin karamana gelhayredd")
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(0.5)