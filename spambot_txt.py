import pyautogui
import time
f=open("xyz.txt",'r')
time.sleep(30)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    