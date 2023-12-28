import keyboard
import mouse
from time import sleep as sl
import pyautogui as pl


sl(4)
def spam():
    score = 1
    text = 'Akmal ban berma bu test'
    while score < 100:
        score = score + 1
        sl(0.01)
        keyboard.write(text)
        sl(0.01)
        keyboard.press_and_release('enter')
        if score > 100:
            break

spam()
