#!/usr/bin/env python3

hostname = input("Hostname: ").strip().lower()
port = int(input("Port: "))

if not hostname:
    print("Hostname Cannot Be Empty")
elif 1 <= port <=65536:
    print(f"Target: {hostname}:{port}")
else:
    print("Invalid Port")
