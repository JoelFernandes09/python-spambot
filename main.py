import pyautogui
import time

time.sleep(5)

msg = "This message will keep spamming"  # Replace this with a message you want to spam
delay = 0.5  # In seconds, change it to a delay you want between the spam
spamTime = 100  # Replace with number of times you want the message to be spammed

for x in range(0, spamTime):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
    time.sleep(delay)

time.sleep(1)
