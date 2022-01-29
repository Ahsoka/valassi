import win32gui

def get_windows(invisible: bool = False):
    windows = []

    def winEnumHandler(hwnd, ctx):
        if invisible or win32gui.IsWindowVisible(hwnd):
            windows.append(hwnd)

    win32gui.EnumWindows(winEnumHandler, None)

    return windows
