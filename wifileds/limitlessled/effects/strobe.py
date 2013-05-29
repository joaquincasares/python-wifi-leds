import time

def run(bulb, duration=10, on_duration=0, off_duration=0):
    # Keep track of time in effect
    start_time = time.time()

    # Main loop
    while True:
        # Flash the lights off, then on
        bulb.all_off()
        time.sleep(off_duration)
        bulb.all_on()

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

        # Leave the bulb on white
        time.sleep(on_duration)
