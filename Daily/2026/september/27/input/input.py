#!/usr/bin/env python3

hostname = input("Hostname: ").lower().strip()
port = int(input("Port"))

if not hostname:
    print("Hostname cannot be empty")
elif 1 <= port <= 65535:
    print(f"Target: {hostname}:{port}")
else:
    print("Invalid Port")
