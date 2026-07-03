import os
from datetime import datetime
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
loops_dir = os.path.join(day_dir, "loops")
lists_dir = os.path.join(day_dir, "lists")
dictionary_dir = os.path.join(day_dir, "dictionary")
function_dir = os.path.join(day_dir, "function")
case_dir = os.path.join(day_dir, "case")
file_dir = os.path.join(day_dir, "file_handling")
while_dir = os.path.join(day_dir, "while")

for path in [input_dir, print_dir, variable_dir, loops_dir, lists_dir, dictionary_dir, function_dir, case_dir, file_dir, while_dir]:
    os.makedirs(path, exist_ok=True)

#======= Cheat Sheets =======#
print_cheatpath = os.path.join(print_dir, "cheatsheet.md")
print_cheatcontent = (
    'print("Hello, World!")\n'
    'print("My name is Cosmos")\n'
    'print("2 + 3 =", 2 + 3)\n'
    'print("This is line one\\nThis is line two")\n'
)

if not os.path.exists(print_cheatpath):
    with open(print_cheatpath, "w") as f:
        f.write(print_cheatcontent)

input_cheatpath = os.path.join(input_dir, "cheatsheet.md")
input_cheatcontent = (
    'name = input("what is your name? ")\n'
    'print(f"Hello, {name}!")'
)

if not os.path.exists(input_cheatpath):
    with open(input_cheatpath, "w") as f:
        f.write(input_cheatcontent)

variable_cheatpath = os.path.join(variable_dir, "cheatsheet.md")
variable_cheatcontent = (
        'x = 10\n'
        'y = 5\n'
        'sum = x + y\n'
        'print("The total is =", sum)'
)

if not os.path.exists(variable_cheatpath):
    with open(variable_cheatpath, "w") as f:
        f.write(variable_cheatcontent)

loops_cheatpath = os.path.join(loops_dir, "cheatsheet.md")
loops_cheatcontent = (
    'for i in range(5):\n'
    '   print("Loop Number:", i)\n'
)

if not os.path.exists(loops_cheatpath):
    with open(loops_cheatpath, "w") as f:
        f.write(loops_cheatcontent)

lists_cheatpath = os.path.join(lists_dir, "cheatsheet.md")
lists_cheatcontent = (
    'fruits = ["apple", "banana", "cherry"]\n'
    'print(fruits[0])\n'
    'fruit.append("orange")\n'
    'print(f"Updated Fruits: {fruits}")\n'
)

if not os.path.exists(lists_cheatpath):
    with open(lists_cheatpath, "w") as f:
        f.write(lists_cheatcontent)

dictionary_cheatpath = os.path.join(dictionary_dir, "cheatsheet.md")
dictionary_cheatcontent = (
    'person = {"name": "Cosmos", "age": "29", "city": "Pleasanton"}\n'
    'print(person["name"])'
)

if not os.path.exists(dictionary_cheatpath):
    with open(dictionary_cheatpath, "w") as f:
        f.write(dictionary_cheatcontent)

function_cheatpath = os.path.join(function_dir, "cheatsheet.md")
function_cheatcontent = (
    'def greet(name):\n'
    '   print(f"Hello, {name}")\n\n'
    'greet("Cosmos")'
)

if not os.path.exists(function_cheatpath):
    with open(function_cheatpath, "w") as f:
        f.write(function_cheatcontent)

case_cheatpath = os.path.join(case_dir, "cheatsheet.md")
case_cheatcontent = (
    'def greet(language):\n'
    '   print("1. English")\n\n'
	'   language = input("Entry: ").lower()\n\n\n'
	'   print(language)'
	'greet()'
)

if not os.path.exists(case_cheatpath):
    with open(case_cheatpath, "w") as f:
        f.write(case_cheatcontent)

file_cheatpath = os.path.join(file_dir, "cheatsheet.md")
file_cheatcontent = (
    'with open("notes.txt", "w") as f:\n'
    '   f.write("this is my first file!")'
)

if not os.path.exists(file_cheatpath):
    with open(file_cheatpath, "w") as f:
        f.write(file_cheatcontent)

while_cheatpath = os.path.join(while_dir, "cheatsheet.md")
while_cheatcontent = (
    'import subprocess\n\n'
    'while True:\n'
    '    subprocess.run([\n'
    '        "ping", "-c", "4", "8.8.8.8"\n'
    '    ])\n'
    '    break\n'
)

if not os.path.exists(while_cheatpath):
    with open(while_cheatpath, "w") as f:
        f.write(while_cheatcontent)

print(f"Created daily folder structure for {today.strftime('%Y-%m%d')}")
