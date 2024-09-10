import ctypes,sys
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


def HwndFromTitle(string):
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

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long)
    ]

# Load user32.dll
user32 = ctypes.windll.user32

def get_geometry(hwnd):
    """
    Gets the geometry of the window with the given hwnd.

    Args:
        hwnd (int): The handle to the window (HWND).
    
    Returns:
        tuple: A tuple containing (x, y, width, height) of the window.
    """
    rect = RECT()
    result = user32.GetWindowRect(hwnd, ctypes.byref(rect))
    if not result:
        return None

    x = rect.left
    y = rect.top
    width = rect.right - rect.left
    height = rect.bottom - rect.top

    return x, y, width, height