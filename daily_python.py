#!/usr/bin/env python3

import os
import sys
from datetime import datetime

# Add Signal_Link.py Path to File
sys.path.append("/opt/signal_link")

from signal_link import signal_link

base_dir = "/home/cosmos/Python/Daily"

today = datetime.now()
year = today.strftime("%Y")
month = today.strftime("%B").lower()
day = today.strftime("%d").lstrip("0")

# Standard Library Excersises #
day_dir = os.path.join(base_dir, year, month, day)
input_dir = os.path.join(day_dir, "input")
print_dir = os.path.join(day_dir, "print")
variable_dir = os.path.join(day_dir, "variable")
requests_dir = os.path.join(day_dir, "requests")
lists_dir = os.path.join(day_dir, "lists")
dictionary_dir = os.path.join(day_dir, "dictionary")
function_dir = os.path.join(day_dir, "function")
case_dir = os.path.join(day_dir, "case")
file_dir = os.path.join(day_dir, "file_handling")
subprocess_dir = os.path.join(day_dir, "subprocess")

for path in [input_dir, print_dir, variable_dir, requests_dir, lists_dir, dictionary_dir, function_dir, case_dir, file_dir, subprocess_dir]:
    os.makedirs(path, exist_ok=True)

#======= Cheat Sheets =======#
print_cheatpath = os.path.join(print_dir, "cheatsheet.md")
print_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'name = "cosmos"\n'
    'status = "online"\n'
    'users = 42\n\n'
    'print(f"User: {name}")\n'
    'print(f"Status: {status} | Users: {users}")\n'
    'print("server", "status", "users", sep=" | ")\n'
    "print(f\"{'Server':<15} {'Status':<10} {'Users':>5}\")"
)

if not os.path.exists(print_cheatpath):
    with open(print_cheatpath, "w") as f:
        f.write(print_cheatcontent)

input_cheatpath = os.path.join(input_dir, "cheatsheet.md")
input_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'hostname = input("Hostname: ").strip().lower()\n'
    'port = int(input("Port: "))\n\n'
    'if not hostname:\n'
    '   print("Hostname cannot be empty.")\n'
    'elif 1 <= port <=65535:\n'
    '   print(f"Target: {hostname}:{port}")\n'
    'else:\n'
    '   print("Invalid Port")'
)

if not os.path.exists(input_cheatpath):
    with open(input_cheatpath, "w") as f:
        f.write(input_cheatcontent)

variable_cheatpath = os.path.join(variable_dir, "cheatsheet.md")
variable_cheatcontent = (
        '#!/usr/bin/env python3\n\n'
        'hostname = "web01"\n'
        'ip_address = "10.0.0.25"\n'
        'port = 443\n'
        'is_online = True\n\n'
        'print(f"{hostname} | {ip_address}:{port} | Online: {is_online}")'
)

if not os.path.exists(variable_cheatpath):
    with open(variable_cheatpath, "w") as f:
        f.write(variable_cheatcontent)

requests_cheatpath = os.path.join(requests_dir, "cheatsheet.md")
requests_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'import requests\n\n'
    'response = requests.get("https://httpbin.org/get")\n\n'
    'print(response.status_code)\n'
    'print(response.text)\n'
)

if not os.path.exists(requests_cheatpath):
    with open(requests_cheatpath, "w") as f:
        f.write(requests_cheatcontent)

lists_cheatpath = os.path.join(lists_dir, "cheatsheet.md")
lists_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'servers  = [\n'
    '   "web01",\n'
    '   "db01",\n'
    ']\n\n'
    'for server in servers:\n'
    '   print(f"Checking: {server}")'
)

if not os.path.exists(lists_cheatpath):
    with open(lists_cheatpath, "w") as f:
        f.write(lists_cheatcontent)

dictionary_cheatpath = os.path.join(dictionary_dir, "cheatsheet.md")
dictionary_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'server = {\n'
    '   "hostname": "web01",\n'
    '   "ip": "10.0.0.25",\n'
    '   "port": 443,\n'
    '   "online": True\n'
    '}\n\n'
    'print(server["hostname"])\n'
    'print(server["ip"])\n'
    'print(server["online"])'
)

if not os.path.exists(dictionary_cheatpath):
    with open(dictionary_cheatpath, "w") as f:
        f.write(dictionary_cheatcontent)

function_cheatpath = os.path.join(function_dir, "cheatsheet.md")
function_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'def check_port(hostname, port):\n'
    '   return f"Checking {hostname}:{port}"\n\n'
    'result = check_port("web01", 443)\n\n'
    'print(result)'
)

if not os.path.exists(function_cheatpath):
    with open(function_cheatpath, "w") as f:
        f.write(function_cheatcontent)

case_cheatpath = os.path.join(case_dir, "cheatsheet.md")
case_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'def menu():\n'
    '    print("[1] Check server")\n'
    '    print("[2] Restart service")\n'
    '    print("[q] Quit")\n\n'
    '    choice = input("Entry: ").strip().lower()\n\n'
    '    if choice == "1":\n'
    '        print("Checking server...")\n'
    '    elif choice == "2":\n'
    '        print("Restarting service...")\n'
    '    elif choice == "q":\n'
    '        return\n'
    '    else:\n'
    '        print("Invalid option.")\n\n'
    'menu()\n'
)

if not os.path.exists(case_cheatpath):
    with open(case_cheatpath, "w") as f:
        f.write(case_cheatcontent)

file_cheatpath = os.path.join(file_dir, "cheatsheet.md")
file_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'with open("boogers.md", "w") as f:\n'
    '    f.write("web01\\n")\n\n'
    'with open("boogers.md", "a") as f:\n'
    '    f.write("db01\\n")\n\n'
    'with open("boogers.md", "r") as f:\n'
    '    print(f.read())\n'
)

if not os.path.exists(file_cheatpath):
    with open(file_cheatpath, "w") as f:
        f.write(file_cheatcontent)

subprocess_cheatpath = os.path.join(subprocess_dir, "cheatsheet.md")
subprocess_cheatcontent = (
    '#!/usr/bin/env python3\n\n'
    'import subprocess\n\n'
    'result = subprocess.run(\n'
    '    ["ping", "-c", "4", "8.8.8.8"],\n'
    '    capture_output=True,\n'
    '    text=True\n'
    ')\n\n'
    'print("Return code:", result.returncode)\n'
    'print(result.stdout)\n'
)

if not os.path.exists(subprocess_cheatpath):
    with open(subprocess_cheatpath, "w") as f:
        f.write(subprocess_cheatcontent)

print(f"Created daily folder structure for {today.strftime('%Y-%m%d')}")

signal_link("daily_python.py", "dailybox-prod-LXC")
