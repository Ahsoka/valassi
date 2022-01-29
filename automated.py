from send_keys import key_press, context_key_press
import mouse
import time

def open_sealed_caches(number: int):
    for num in range(number):
        print(f"Opening Cache {num + 1}")
        key_press('f', 1.75)
        time.sleep(2)
        key_press('space', 0.1)

def buy_items():
    NUM_OF_ITEMS_TO_BUY = 60
    TOTAL_RUNS = 2

    for count in range(TOTAL_RUNS):
        time.sleep(0.5)
        key_press("f", .5)
        print(count)

        key_press('s', 2.5)

        time.sleep(1.5)
        for i in range(NUM_OF_ITEMS_TO_BUY):
            time.sleep(0.1)
            print(i)
            key_press("space")
            time.sleep(0.65)
            key_press("space")

        key_press("esc")

        time.sleep(0.5)

        key_press("b")
        time.sleep(0.5)

        key_press('s', 1)
        key_press("enter")
        time.sleep(0.5)

        with context_key_press('left-shift'):
            mouse.move(2091, 414)
            mouse.press()
            mouse.move(2069, 851)
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
