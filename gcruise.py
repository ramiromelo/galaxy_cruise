from pynput import keyboard

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