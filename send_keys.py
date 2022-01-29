from send_input import PressKey, ReleaseKey
from keys import keys
import contextlib


@contextlib.contextmanager
def context_key_press(key: str):
    if key not in keys:
        raise ValueError(f"'{key}' is not a valid key! See keys dictionary for valid keys.")
    try:
        PressKey(keys[key])
        yield
    finally:
        ReleaseKey(keys[key])
