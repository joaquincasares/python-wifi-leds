import random
import time

def run(bridge, duration=15, max_on_duration=0, max_off_duration=0.1, max_stutter=4,
        colors=['red', 'royal_blue', 'white']):
    '''An effect that simulates United States police flashers.

    Keyword arguments:
    bridge -- the bridge that will be controlled (required)
    duration -- length of time the effect will last (default 15)
    max_on_duration -- max length of time possible for the lights to remain in the on position (default 0)
    max_off_duration -- max length of time possible for the lights to remain in the off position (default 0.1)
    max_stutter -- max amount of times that an event will loop (default 4)
    colors -- list of possible colors to choose from (default: ['red', 'royal_blue', 'white']])
              `None`: Random selection of colors
    '''

    # Keep track of time in effect
    start_time = time.time()

    if colors:
        # Set white to be easily accessible via mode_down()
        if 'white' in colors:
            bridge.white()
            bridge.max_brightness()

        # Choose a color in colors to properly set max_brightness
        for color in colors:
            if color != 'white':
                bridge.set_color(color)
                bridge.max_brightness()
                break

    # Main loop
    while True:
        # Flash the lights off, then on
        if max_off_duration:
            # Possibly repeat the lights off effect
            this_stutter_count = random.random() * max_stutter
            i = 0
            while i < this_stutter_count:
                bridge.all_off()

                # Keep lights off for random length of time
                time.sleep(random.random() * max_off_duration)

                bridge.all_on()
                i += 1

        # Possibly repeat the color changing effect
        this_stutter_count = random.random() * max_stutter
        i = 0
        while i < this_stutter_count:
            if colors:
                # If colors are provided, choose a specified color
                current_color = colors[int(random.random() * len(colors))]
                if current_color == 'white':
                    bridge.white()
                else:
                    bridge.set_color(current_color)
            else:
                # If colors are NOT provided, choose a random color
                bridge.set_color_hex(chr(int(random.random() * 255)))

            # Keep lights off for random length of time
            time.sleep(random.random() * max_on_duration)
            i += 1

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

