import time

def run(bulb, delay=0.0, duration=10):
    start_time = time.time()
    while True:
        bulb.all_off()
        bulb.short_pause()
        bulb.all_on()
        bulb.short_pause()

        if time.time() - start_time > duration:
            break

        time.sleep(delay)
