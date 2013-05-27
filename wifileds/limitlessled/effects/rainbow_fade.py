import time

def run(bulb, delta=1, delay=0.0):
    delta = int(delta)
    if delta == 0:
        raise RuntimeError('rainbow_fade:delta value cannot be 0')

    i = 0
    max_loop = 256
    while i < max_loop:
        bulb.set_color_hex(chr(i))
        bulb.short_pause()

        i += delta
        if i == max_loop:
            break

        time.sleep(delay)
