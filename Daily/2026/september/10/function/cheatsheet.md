#!/usr/bin/env python3

def check_port(hostname, port):
   return f"Checking {hostname}:{port}"

result = check_port("web01", 443)

print(result)