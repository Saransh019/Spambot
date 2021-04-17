import pyautogui
import webbrowser as wb
import time
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
wb.get(chrome_path).open('https://web.whatsapp.com/')
time.sleep(30)
for i in range(150):
    pyautogui.typewrite("Hello Bewakoof!")
    pyautogui.press("enter")