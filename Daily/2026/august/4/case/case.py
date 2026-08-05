#!/usr/bin/env python3

def greet():
    print("1. English")
    print("q. Quit")

    language = input("what is your name? ").lower()

    if language == "q":
        return

    print(language)

greet()
