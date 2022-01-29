import win32gui

def get_windows(invisible: bool = False):
    windows = []

    def winEnumHandler(hwnd, ctx):
        if invisible or win32gui.IsWindowVisible(hwnd):
            windows.append(hwnd)

    win32gui.EnumWindows(winEnumHandler, None)

    return windows

def focus_division():
    the_division = next(filter(
        lambda hwnd: win32gui.GetWindowText(hwnd) == "Tom Clancy's The Division",
        get_windows()
    ))
    win32gui.SetForegroundWindow(the_division)
