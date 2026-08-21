#!/usr/bin/env python3

def greet():
    print("1. Greet")

    print("[q] Quit")

    language = input("Entry: ")

    if language == "q":
        return

    print(language)

greet()
