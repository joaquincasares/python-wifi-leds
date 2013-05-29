import random
import time

def run(bridge, duration=10, max_on_duration=1, max_off_duration=1, max_stutter=4,
        colors=['red', 'royal_blue', 'white']):

    # Keep track of time in effect
    start_time = time.time()

    if colors:
        # Set white to be easily accessible via mode_down()
        if 'white' in colors:
            bridge.white()

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

        # Possibly repeat the color changing effect
        this_stutter_count = random.random() * max_stutter
        i = 0
        while i < this_stutter_count:
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

            # Keep lights off for random length of time
            time.sleep(random.random() * max_on_duration)

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

