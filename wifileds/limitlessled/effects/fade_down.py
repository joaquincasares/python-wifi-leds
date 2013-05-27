import time

def run(bulb, delay=0.0):
    i = 0
    max_loop = 9
    while i < max_loop:
        bulb.brightness_down()
        bulb.short_pause()

        i += 1
        if i == max_loop:
            break

        time.sleep(delay)
