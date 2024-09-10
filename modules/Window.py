import ctypes
from ctypes import wintypes

# Define necessary types and functions from user32.dll
user32 = ctypes.windll.user32
EnumWindows = user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowTextW = user32.GetWindowTextW
GetWindowTextLengthW = user32.GetWindowTextLengthW
IsWindowVisible = user32.IsWindowVisible

# Function to list all windows and their handles
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):  # Only consider visible windows
        length = GetWindowTextLengthW(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowTextW(hwnd, buff, length + 1)
        print(f"Window Handle: {hwnd}, Window Title: {buff.value}")
    return True

# Initialize EnumWindows and run it with the callback function
def list_windows():
    EnumWindows(EnumWindowsProc(foreach_window), 0)


def HwndContains(string):
    selectedHwnd = None
    def NameMatches(hwnd, lParam):
        if IsWindowVisible(hwnd):  # Only consider visible windows
            length = GetWindowTextLengthW(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowTextW(hwnd, buff, length + 1)
            print(f"Window Handle: {hwnd}, Window Title: {buff.value}")
            if string in buff.value:
                selectedHwnd = hwnd
                return False
        return True
    EnumWindows(EnumWindowsProc(NameMatches), 0)
    return selectedHwnd