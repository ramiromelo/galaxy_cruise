from pynput import keyboard
import pyautogui, sys

#NEXT GALAXY (N)
def on_activate_n():
    print('NEXT GALAXY')
    pyautogui.moveTo(1760, 810)

def on_activate_a():
    print('A pressed')

def on_activate_b():
    print('B pressed')

def on_activate_c():
    print('C pressed')

def quit():
    print('QUIT')
    h.stop()

with keyboard.GlobalHotKeys({
        'a': on_activate_a,
        'b': on_activate_b,
        'c': on_activate_c,
        '<ctrl>+c': quit}) as h:
    h.join()

