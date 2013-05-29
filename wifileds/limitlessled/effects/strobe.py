import time

def run(bridge, duration=10, on_duration=0, off_duration=0):
    # Keep track of time in effect
    start_time = time.time()

    # Main loop
    while True:
        # Flash the lights off, then on
        bridge.all_off()
        time.sleep(off_duration)
        bridge.all_on()

        # Check if effect duration has past
        if time.time() - start_time > duration:
            break

        # Leave the bridge on white
        time.sleep(on_duration)
