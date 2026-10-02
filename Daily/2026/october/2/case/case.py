#!/usr/bin/env python3

def menu():
    print("[1] Check Server")
    print("[2] Restart Service")
    print("[q] Quit")

    choice = input("Entry: ").strip().lower()

    if choice == "1":
        print("checking server...")
    elif choice == "2":
        print("restarting service...")
    elif choice == "q":
        return
    else:
        print("Invalid Option")

menu()
