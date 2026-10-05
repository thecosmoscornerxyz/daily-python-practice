#!/usr/bin/env python3

def menu():
    print("[1] Check server")
    print("[2] Restart service")
    print("[q] Quit")

    choice = input("Entry: ").strip().lower()

    if choice == "1":
        print("Checking server...")
    elif choice == "2":
        print("Restarting service...")
    elif choice == "q":
        return
    else:
        print("Invalid option.")

menu()
