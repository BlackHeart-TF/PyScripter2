import ctypes
import time
class Key():
    hwnd = None

    def __init__(self, hwnd):
        Key.hwnd = hwnd

    @classmethod
    def Press(self,key_code):
        if not Key.hwnd:
            raise Exception("No hwnd set")
        ctypes.windll.user32.PostMessageW(Key.hwnd, 0x0100, self.get_vk_code(key_code), 0)
        
    @classmethod        
    def Release(self,key_code):
        if not Key.hwnd:
            raise Exception("No hwnd set")
        ctypes.windll.user32.PostMessageW(Key.hwnd, 0x0101, self.get_vk_code(key_code), 0)
    
    @classmethod
    def Send(self,code,delay_ms=10):
        self.Press(code)
        time.delay_ms(delay_ms)
        self.Release(code)
    
    @classmethod
    def get_vk_code(self,char):
        if isinstance(char,int):
            return char
        # VkKeyScanW takes a character and returns the virtual key code
        vk_code = ctypes.windll.user32.VkKeyScanW(ord(char))
        # The low-order byte is the virtual key code
        return vk_code & 0xFF