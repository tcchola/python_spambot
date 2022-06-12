import pyautogui
import time

time.sleep(6)  # Wait 6 seconds

script = open("script.txt", 'r')

for word in script:
    pyautogui.typewrite(word)  #  Write the word in a text box
    pyautogui.press("enter")   #  Send
