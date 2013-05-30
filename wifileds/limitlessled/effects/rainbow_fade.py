import time

def run(bridge, duration=15, delta=1, delay=0):
    '''Fade down the light at a specified delay.

    Keyword arguments:
    bridge -- the bridge that will be controlled (required)
    duration -- length of time the effect will last (default 15)
    delta -- amount of change between colors (default 1)
             Requirement: delta > 1
    delay -- delay between fade commands (default 0)
    '''

    # Keep track of time in effect
    start_time = time.time()

    # Ensure we do not get an infinite loop
    delta = int(delta)
    if delta == 0:
        raise RuntimeError('rainbow_fade:delta value cannot be 0')

    # Max selction of colors possible
    max_colors = 256

    # Main loop
    i = 0
    while True:
        bridge.set_color_hex(chr(i))

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

        time.sleep(delay)
        i = (delta + i) % max_colors
