import time
from pynput import keyboard
import pyautogui, sys

#NEXT GALAXY (N)
def on_activate_next():
    print('NEXT GALAXY')
    pyautogui.moveTo(1760, 810)
    pyautogui.click()
    pyautogui.moveTo(960, 540)
    time.sleep(.1)
    pyautogui.scroll(100)
    pyautogui.scroll(100)
    pyautogui.scroll(100)
    pyautogui.scroll(100)
    pyautogui.scroll(100)

#ZOOM
def on_activate_zoom():
    pyautogui.moveTo(960, 540)
    time.sleep(.1)
    pyautogui.scroll(100)
    pyautogui.scroll(100)
    pyautogui.scroll(100)
    pyautogui.scroll(100)
    pyautogui.scroll(100)

#SPIRAL GALAXY
def on_activate_spiral():
    print('SPIRAL GALAXY')
    pyautogui.moveTo(830, 830)
    pyautogui.click()

#ELLIPTICAL GALAXY
def on_activate_elliptical():
    print('ELLIPTICAL GALAXY')
    pyautogui.moveTo(1000, 830)
    pyautogui.click()

#NEITHER
def on_activate_neither():
    print('NEITHER')
    pyautogui.moveTo(1120, 880)
    pyautogui.click()

#INTERACTING
def on_activate_i():
    print('INTERACTING')
    pyautogui.moveTo(830, 830)
    pyautogui.click()

#NOT INTERACTING
def on_activate_not():
    print('NOT INTERACTING')
    pyautogui.moveTo(1000, 840)
    pyautogui.click()

#TAILS
def on_activate_tails():
    print('TAILS')
    pyautogui.moveTo(1000, 840)
    pyautogui.click()

#DISTORTION
def on_activate_distortion():
    print('DISTORTION')
    pyautogui.moveTo(1170, 830)
    pyautogui.click()

#SUBMIT 1
def on_activate_1():
    print('SUBMIT 1')
    pyautogui.moveTo(960, 880)
    pyautogui.click()

#SUBMIT 5
def on_activate_5():
    print('SUBMIT 5')
    pyautogui.moveTo(1300, 880)
    pyautogui.click()

#SUBMIT
def on_activate_submit():
    print('SUBMIT')
    pyautogui.moveTo(1300, 880)
    pyautogui.click()
    pyautogui.moveTo(960, 880)
    pyautogui.click()
    

def quit():
    print('QUIT')
    h.stop()

with keyboard.GlobalHotKeys({
        '-': on_activate_next,
        'z': on_activate_zoom,
        's': on_activate_spiral,
        'e': on_activate_elliptical,
        '/': on_activate_neither,
        'i': on_activate_i,
        'n': on_activate_not,
        't': on_activate_tails,
        'd': on_activate_distortion,
        '1': on_activate_1,
        '5': on_activate_5,
        'u': on_activate_submit,
        '<ctrl>+c': quit}) as h:
    h.join()

