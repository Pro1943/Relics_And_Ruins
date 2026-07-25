import ctypes as ct
from ctypes import wintypes
import sys
import subprocess
import os

kernel32 = ct.WinDLL('kernel32', use_last_error=True)
user32 = ct.WinDLL('user32', use_last_error=True)

kernel32.GetConsoleWindow.argtypes = []
kernel32.GetConsoleWindow.restype = wintypes.HWND

user32.GetWindowRect.argtypes = [wintypes.HWND, wintypes.LPRECT]
user32.GetWindowRect.restype = wintypes.BOOL

user32.GetSystemMetrics.argtypes = [ct.c_int]
user32.GetSystemMetrics.restype = ct.c_int

user32.MoveWindow.argtypes = [wintypes.HWND, ct.c_int, ct.c_int, ct.c_int, ct.c_int, wintypes.BOOL]
user32.MoveWindow.restype = wintypes.BOOL

kernel32.GetShortPathNameW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD]
kernel32.GetShortPathNameW.restype = wintypes.DWORD

SM_CXSCREEN = 0
SM_CYSCREEN = 1

def get_short_path(long_path):
    buf = ct.create_unicode_buffer(260)
    kernel32.GetShortPathNameW(long_path, buf, 260)
    return buf.value

def console_config(target_width, target_height):
    kernel32.SetConsoleTitleW("Relics and Ruins")
    hwnd = kernel32.GetConsoleWindow()
    
    if "LAUNCHED_BY_GAME" not in os.environ:
        current_env = os.environ.copy()
        current_env["LAUNCHED_BY_GAME"] = "1"
        
        raw_script_path = os.path.abspath(sys.argv[0])
        script_path = get_short_path(raw_script_path)
        python_exe = get_short_path(sys.executable)
        
        command_string = f"{python_exe} {script_path}"
        command_list = ["cmd.exe", "/k", command_string]
        
        subprocess.Popen(command_list, creationflags=subprocess.CREATE_NEW_CONSOLE, env=current_env)
        sys.exit(0)
        
    h_input = kernel32.GetStdHandle(-10)
    mode = wintypes.DWORD()
    kernel32.GetConsoleMode(h_input, ct.byref(mode))
    new_mode = (mode.value & ~0x0040) | 0x0080
    kernel32.SetConsoleMode(h_input, new_mode)
    
    screen_width = user32.GetSystemMetrics(SM_CXSCREEN)
    screen_height = user32.GetSystemMetrics(SM_CYSCREEN)
    
    rect = wintypes.RECT()
    user32.GetWindowRect(hwnd, ct.byref(rect))
    
    new_x = (screen_width - target_width) // 2
    new_y = (screen_height - target_height) // 2
    
    user32.MoveWindow(hwnd, new_x, new_y, target_width, target_height, True)
