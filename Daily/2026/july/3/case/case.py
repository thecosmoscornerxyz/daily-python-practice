#!/usr/bin/env python3

def greet(language):
    match language:
        case "English":
            print("Hello!")
        case _:
            print("Language Not Recognized")

greet("English")
