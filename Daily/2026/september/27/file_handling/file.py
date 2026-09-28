#!/usr/bin/env python3

with open("boogers.txt", "w") as f:
    f.write("web01\n")

with open("boogers.txt", "a") as f:
    f.write("db01\n")

with open("boogers.txt", "r") as f: 
    print(f.read())
