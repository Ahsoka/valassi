from send_keys import key_press
import time

def open_sealed_caches(number: int):
    for num in range(number):
        print(f"Opening Cache {num + 1}")
        key_press('f', 1.75)
        time.sleep(2)
        key_press('space', 0.1)

def buy_items(number_of_items: int):
    for count in range(22):
        print(count)
        time.sleep(0.5)
        key_press("f", .5)

        # choose which item to buy based on arrow key
        item_range = 6
        for i in range(item_range):
            time.sleep(0.000001)
            key_press("s")

        # time.sleep(1.5)
        backpack_size = 45
        for i in range(backpack_size):
            time.sleep(0.00001)
            # print(i)
            key_press("space")
            time.sleep(0.5)
            key_press("space")

        key_press("esc")

        time.sleep(0.5)

        key_press("b")
        time.sleep(0.5)

        time.sleep(0.5)
        key_press("s")
        time.sleep(0.000001)
        key_press("s")

        # uncomment below for tool
        time.sleep(0.000001)
        key_press("s")


        time.sleep(0.000001)
        key_press("enter")
        time.sleep(0.5)

        # comment below out for tool
        # key_press("s")
        # time.sleep(0.000001)

        for i in range(45):
            # print(i)
            key_press("v")
            time.sleep(0.000001)

        key_press("x", 1)

        time.sleep(0.000001)

        key_press("space")
        time.sleep(0.000001)
        key_press("esc")
        time.sleep(0.000001)
        key_press("esc")
        time.sleep(0.000001)
        key_press("esc")
        time.sleep(0.000001)
