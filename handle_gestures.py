import json
import sys
from pynput.keyboard import Key, Controller

sys.path.insert(1, './scripts')

def gesture_identifier(angles):
    activated = [1 if i<120 else 0 for i in angles]
    activated_fingers = [i for i, x in enumerate(activated) if x == 1]
    return activated_fingers

def handle_scripts(function, last_executed):
    with open('register.json') as register:
        functions = json.load(register)
        if last_executed == function:
            pass
        elif function in functions.keys():
            try:
                exec(f'import {functions[function]}')
                exec(f'{functions[function]}.run()')
            except SyntaxError:
                print('Error: that gesture is not assigned')

    return function

def gesture_handler(activated_fingers, last_executed, scripts):
    """
    0 - thumb
    1 - index
    2 - middle
    3 - ring
    4 - pinky
    """

    function = str(''.join([str(i) for i in activated_fingers]))

    if scripts:
        function = handle_scripts(function, last_executed)


    return function
