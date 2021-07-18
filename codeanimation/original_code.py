import pyautogui
import time


with open ('code.txt', 'r') as f:
    file_lines = f.readlines()

for i in range(10, 1, -1):
    time.sleep(1)
    print(f'Starting auto coding in {i} seconds ...')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('a')
pyautogui.keyUp('a')
pyautogui.keyUp('ctrl')
pyautogui.keyDown('delete')
pyautogui.keyUp('delete')

for line in file_lines:
    for ch in line:
        pyautogui.typewrite(ch)

    # Use shift tab a couple of times and wait
    if line != '\n':
        time.sleep(0.25)
        pyautogui.keyDown('shift')
        for _ in range(8):
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')

        pyautogui.keyUp('shift')

