import time

def run(bridge, delay=0):
    '''Fade down light at a specified delay.

    Keyword arguments:
    bridge -- the bridge that will be controlled (required)
    delay -- delay between fade down commands (default 0)
    '''

    # Number of steps between min and max
    max_loop = 9

    # Main loop
    i = 0
    while i < max_loop:
        bridge.brightness_down()

        i += 1
        if i == max_loop:
            break

        time.sleep(delay)
