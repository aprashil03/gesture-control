import json
import sys
sys.path.insert(1, './scripts')

def gesture_identifier(angles, last_executed):
    activated = [1 if i<120 else 0 for i in angles]
    activated_fingers = [i for i, x in enumerate(activated) if x == 1]
    return gesture_handler(activated_fingers, last_executed)

def gesture_handler(activated_fingers, last_executed):
    """
    0 - thumb
    1 - index
    2 - middle
    3 - ring
    4 - pinky
    """

    function = str(''.join([str(i) for i in activated_fingers]))

    with open('register.json') as register:
        functions = json.load(register)
        if last_executed == function:
            pass
        elif function in functions.keys():
            print(functions, function)
            print(f'import {functions[function]}')


    return function
