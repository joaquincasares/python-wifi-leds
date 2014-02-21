import random
import time

def run(bridge, duration=15, fade_up_delay=0, fade_down_delay=0.01, on_duration=0.5, off_duration=0,
        colors=['yellow'], color_changes=True):
    '''An effect that simulates yellow factory warning flashers.

    Keyword arguments:
    bridge -- the bridge that will be controlled (required)
    duration -- length of time the effect will last (default 15)
    fade_up_delay -- delay between fade up commands (default 0)
    fade_down_delay -- delay between fade down commands (default 0.01)
    on_duration -- length of time for the lights to remain in the on position (default 0.5)
    off_duration -- length of time for the lights to remain in the off position (default 0)
    colors -- list of possible colors to choose from (default: ['yellow']])
              `None`: Random selection of colors
    color_changes -- boolean that judges if colors will be changed inside the effect (default True)
    '''

    # Keep track of time in effect
    start_time = time.time()

    if color_changes:
        # Set white to be easily accessible via mode_down()
        if 'white' in colors:
            bridge.white()

    # Main loop
    while True:
        # Flash the lights off, then on
        bridge.all_off()
        time.sleep(off_duration)
        bridge.all_on()

        if color_changes:
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

        
        # Swell lights to max brightness
        if hasattr(bridge, 'set_brightness') and callable(getattr(bridge, 'set_brightness')):
            for i in range(2,28):
                bridge.set_brightness(i)
                time.sleep(fade_up_delay)
        else:
            for i in range(0, 9):
                bridge.brightness_up()
                time.sleep(fade_up_delay)

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

        time.sleep(on_duration)

        # Swell lights to min brightness
        if hasattr(bridge, 'set_brightness') and callable(getattr(bridge, 'set_brightness')):
            for i in range(2,28):
                bridge.set_brightness(29-i)
                time.sleep(fade_down_delay)
        else:
            for i in range(0, 9):
                bridge.brightness_down()
                time.sleep(fade_down_delay)
