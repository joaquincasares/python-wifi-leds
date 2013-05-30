import random
import time

def run(bridge, duration=15, on_duration=0.3, off_duration=0.01,
        colors=None):
    '''A colorful strobe light effect.

    Keyword arguments:
    bridge -- the bridge that will be controlled (required)
    duration -- length of time the effect will last (default 15)
    on_duration -- length of time the lights remain in the on position (default 0.3)
    off_duration -- length of time the lights remain in the off position (default 0.01)
    colors -- list of possible colors to choose from (default: None)
              `None`: Random selection of colors
    '''
    # Keep track of time in effect
    start_time = time.time()

    if colors:
        # Set white to be easily accessible via mode_down()
        if 'white' in colors:
            bridge.white()

    # Main loop
    while True:
        # Flash the lights off, then on
        if off_duration:
            bridge.all_off()
            time.sleep(off_duration)
            bridge.all_on()

        if colors:
            # If colors are provided, choose a specified color
            current_color = colors[int(random.random() * len(colors))]
            if current_color == 'white':
                bridge.mode_down()
            else:
                bridge.set_color(current_color)
        else:
            # If colors are NOT provided, choose a random color
            bridge.set_color_hex(chr(int(random.random() * 255)))

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

        # Leave the bridge on the same color
        time.sleep(on_duration)
