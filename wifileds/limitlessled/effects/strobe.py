import time

def run(bridge, duration=15, on_duration=0, off_duration=0):
    '''An effect that yellow factory warning flashers.

    Keyword arguments:
    bridge -- the bridge that will be controlled (required)
    duration -- length of time the effect will last (default 15)
    on_duration -- length of time for the lights to remain in the on position (default 0)
    off_duration -- length of time for the lights to remain in the off position (default 0)
    '''

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
