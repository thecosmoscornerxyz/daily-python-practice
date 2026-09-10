#!/usr/bin/env python3

def menu():
    print("[1] Check Server")
    print("[2] Restart Service")
    print(" ")
    print("[q] Quit")

    choice = input("Entry: ").strip().lower()

    if choice == "1":
        print("Checking Server....")
    elif choice == "2":
        print("Restarting Service...")
    elif choice == "q":
        return
    else:
        print("Invalid Option")

menu()
