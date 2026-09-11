#!/usr/bin/env python3

with open("boogers.md", "w") as f:
    f.write("web01\n")

with open("boogers.md", "a") as f:  
    f.write("db01\n")

with open("boogers.md", "r") as f:
    print(f.read())
