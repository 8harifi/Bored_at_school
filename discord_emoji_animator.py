import pyautogui
import time

texts = input(">>").split()
num = int(input("number>>"))

time.sleep(3)

for i in range(num):
    pyautogui.press("up")
    time.sleep(0.5)
    pyautogui.keyDown("ctrl")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.keyUp("ctrl")
    time.sleep(0.5)
    # pyautogui.press("ctrl", "backspace")
    pyautogui.write(texts[i%len(texts)])
    pyautogui.press("enter")
    time.sleep(1.5)
