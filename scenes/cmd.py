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

user32.GetWindowLongW.argtypes = [wintypes.HWND, ct.c_int]
user32.GetWindowLongW.restype = ct.c_long

user32.SetWindowLongW.argtypes = [wintypes.HWND, ct.c_int, ct.c_long]
user32.SetWindowLongW.restype = ct.c_long

user32.GetSystemMenu.argtypes = [wintypes.HWND, wintypes.BOOL]
user32.GetSystemMenu.restype = wintypes.HANDLE

user32.DeleteMenu.argtypes = [wintypes.HANDLE, wintypes.UINT, wintypes.UINT]
user32.DeleteMenu.restype = wintypes.BOOL

user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, ct.c_int, ct.c_int, ct.c_int, ct.c_int, wintypes.UINT]
user32.SetWindowPos.restype = wintypes.BOOL

class COORD(ct.Structure):
    _fields_ = [("X", ct.c_short), ("Y", ct.c_short)]

class SMALL_RECT(ct.Structure):
    _fields_ = [("Left", ct.c_short), ("Top", ct.c_short), ("Right", ct.c_short), ("Bottom", ct.c_short)]

class CONSOLE_SCREEN_BUFFER_INFO(ct.Structure):
    _fields_ = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", ct.c_ushort),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize", COORD)
    ]

kernel32.GetConsoleScreenBufferInfo.argtypes = [wintypes.HANDLE, ct.POINTER(CONSOLE_SCREEN_BUFFER_INFO)]
kernel32.GetConsoleScreenBufferInfo.restype = wintypes.BOOL

kernel32.SetConsoleScreenBufferSize.argtypes = [wintypes.HANDLE, COORD]
kernel32.SetConsoleScreenBufferSize.restype = wintypes.BOOL

SM_CXSCREEN = 0
SM_CYSCREEN = 1
GWL_STYLE = -16

WS_MAXIMIZEBOX = 0x00010000
WS_MINIMIZEBOX = 0x00020000
WS_THICKFRAME = 0x00040000

SC_MAXIMIZE = 0xF030
SC_SIZE = 0xF000
MF_BYCOMMAND = 0x00000000

SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
SWP_NOZORDER = 0x0004
SWP_FRAMECHANGED = 0x0020

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
        command_list = ["conhost.exe", "cmd.exe", "/c", command_string]
        
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

    style = user32.GetWindowLongW(hwnd, GWL_STYLE)
    style &= ~WS_MAXIMIZEBOX
    style &= ~WS_MINIMIZEBOX
    style &= ~WS_THICKFRAME
    user32.SetWindowLongW(hwnd, GWL_STYLE, style)

    sys_menu = user32.GetSystemMenu(hwnd, False)
    if sys_menu:
        user32.DeleteMenu(sys_menu, SC_MAXIMIZE, MF_BYCOMMAND)
        user32.DeleteMenu(sys_menu, SC_SIZE, MF_BYCOMMAND)

    user32.SetWindowPos(hwnd, None, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_FRAMECHANGED)

    h_output = kernel32.GetStdHandle(-11)
    csbi = CONSOLE_SCREEN_BUFFER_INFO()
    if kernel32.GetConsoleScreenBufferInfo(h_output, ct.byref(csbi)):
        window_width = csbi.srWindow.Right - csbi.srWindow.Left + 1
        window_height = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
        new_buffer_size = COORD(window_width, window_height)
        kernel32.SetConsoleScreenBufferSize(h_output, new_buffer_size)
