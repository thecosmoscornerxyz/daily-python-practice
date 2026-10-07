#!/usr/bin/env python3

import subprocess

result = subprocess.run(
    ["ping", "-c", "4", "8.8.8.8"],
    capture_output=True,
    text=True
)

print("Return code:", result.returncode)
print(result.stdout)
