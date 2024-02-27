import pyautogui
import pynput
from pynput.keyboard import Listener


def on_press(key):
    
    if key == pynput.keyboard.Key.shift:
        x, y = pyautogui.position()
        print(f'Mouse is at {x}, {y}')
        print(f'Pixel color at {x}, {y} is {pyautogui.screenshot().getpixel((x, y))}')

with Listener(on_press=on_press) as listener:
    listener.join()
