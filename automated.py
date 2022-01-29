from send_keys import key_press, context_key_press

import mouse
import tqdm
import math
import time

def open_sealed_caches(number: int):
    for num in range(number):
        print(f"Opening Cache {num + 1}")
        key_press('f', 1.75)
        time.sleep(2)
        key_press('space', 0.1)

def buy_items(num_of_items: int, bag_space: int = 30):
    with tqdm.tqdm(total=num_of_items) as progress:
        items = iter(range(num_of_items + 1))
        TOTAL_RUNS = math.ceil(num_of_items / bag_space)

        for _ in range(TOTAL_RUNS):
            time.sleep(0.5)
            key_press("f", .5)

            key_press('s', 2.5)

            time.sleep(1.5)
            for i, _ in zip(items, range(bag_space)):
                time.sleep(0.1)
                key_press("space")
                time.sleep(0.65)
                key_press("space")
                progress.update()

            key_press("esc")

            time.sleep(0.5)

            key_press("b")
            time.sleep(0.5)

            key_press('s', 1)
            key_press("enter")
            time.sleep(0.5)

            with context_key_press('left-shift'):
                mouse.move(2165, 422)
                mouse.press()
                mouse.move(2150, 831)
                time.sleep(.5)
                mouse.release()
                mouse.move(1706, 780)
                mouse.click()
                time.sleep(.05)

            key_press("x", 1.2)

            time.sleep(0.000001)

            key_press("space")
            time.sleep(0.000001)
            key_press("esc")
            time.sleep(0.000001)
            key_press("esc")
            time.sleep(0.000001)
            key_press("esc")
            time.sleep(0.000001)
