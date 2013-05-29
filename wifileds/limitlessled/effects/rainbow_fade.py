import time

def run(bridge, delta=1, delay=0):
    # Ensure we do not get an infinite loop
    delta = int(delta)
    if delta == 0:
        raise RuntimeError('rainbow_fade:delta value cannot be 0')

    # Max selction of colors possible
    max_loop = 256

    # Main loop
    i = 0
    while i < max_loop:
        bridge.set_color_hex(chr(i))

        i += delta
        if i == max_loop:
            break

        time.sleep(delay)
