#!/usr/bin/env python3

def menu():
    print("[1] Check Server")
    print("[2] Restart Server")
    print("[q] Quit")

    choice = input("Entry: ").lower().strip()

    if choice == "1":
        print("Checking Server...")
    if choice == "2":
        print("Restarting Service...")
    if choice == "q": 
        return
    else:
        print("Invalid Option")

menu()
