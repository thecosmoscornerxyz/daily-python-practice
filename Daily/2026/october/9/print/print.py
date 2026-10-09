#!/usr/bin/env python3

name = "web01"
status = "status"
users = 42

print(f"User: {name}")
print("Status: {status} | Users: {users}")
print("server", "status", "users", sep=" | ")
print(f"{'Server':<15} {'Status':<10} {'Users':>5}")
