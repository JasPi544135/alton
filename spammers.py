import keyboard
from time import sleep as sl


sl(4)
def spam():
    score = 1
    text = 'Akmal ban berma bu test'
    while score < 10:
        score = score + 1
        sl(0.01)
        keyboard.write(text)
        sl(0.01)
        keyboard.press_and_release('enter')
        if score > 10:
            break

spam()
