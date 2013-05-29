import random
import time

def run(bulb, duration=10, on_duration=1, off_duration=1,
        colors=[]):
    # Keep track of time in effect
    start_time = time.time()

    # Set white to be easily accessible via mode_down()
    if 'white' in colors:
        bulb.white()

    # Main loop
    while True:
        # Flash the lights off, then on
        if off_duration:
            bulb.all_off()
            time.sleep(off_duration)
            bulb.all_on()

        if colors:
            # If colors are provided, choose a specified color
            current_color = colors[int(random.random() * len(colors))]
            if current_color == 'white':
                bulb.mode_down()
            else:
                bulb.set_color(current_color)
        else:
            # If colors are NOT provided, choose a random color
            bulb.set_color_hex(chr(int(random.random() * 255)))

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

        # Leave the bulb on the same color
        time.sleep(on_duration)
