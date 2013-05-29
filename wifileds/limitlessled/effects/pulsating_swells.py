import time

def run(bulb, duration=10, fade_up_delay=0, fade_down_delay=1, on_duration=1, off_duration=0,
        colors=['yellow'], color_changes=True):
    # Keep track of time in effect
    start_time = time.time()

    if color_changes:
        # Set white to be easily accessible via mode_down()
        if 'white' in colors:
            bulb.white()

    # Main loop
    while True:
        # Flash the lights off, then on
        bulb.all_off()
        time.sleep(off_duration)
        bulb.all_on()

        if color_changes:
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

        # Swell lights to max brightness
        for i in range(0, 9):
            self.brightness_up()
            time.sleep(fade_up_delay)

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

        time.sleep(on_duration)

        # Swell lights to min brightness
        for i in range(0, 9):
            self.brightness_down()
            time.sleep(fade_down_delay)
