#!/usr/bin/env python3

import subprocess

while True:
    subprocess.run(
        ["sudo", "ping", "-c", "4", "9.9.9.9"]
    )
    break
