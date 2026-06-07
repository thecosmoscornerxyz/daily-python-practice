#!/usr/bin/env python3

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

# Ollama, sqlite3, beautifulsoup Subdirectory Excersises #
ollama_dir = os.path.join(day_dir, "ollama")
sqlite_dir = os.path.join(day_dir, "sqlite3")
soup_dir = os.path.join(day_dir, "soup")

for path in [input_dir, print_dir, variable_dir, loops_dir, lists_dir, dictionary_dir, function_dir, case_dir, file_dir, ollama_dir, sqlite_dir, soup_dir]:
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
    '   match language:\n'
    '       case "English":\n'
    '           print("Hello!")\n'
    '       case"Spanish":\n'
    '           print("Hola!")\n'
    '       case "Japanese":\n'
    '           print("こんにちは!")\n'
    '       case _:\n'
    '           print("Language not recognized")\n\n'
    'greet("Japenese")'
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

sqlite3_cheatpath = os.path.join(sqlite_dir, "cheatsheet.md")
sqlite3_cheatcontent = (
    '# CREATE DB #\n\n'
    'import sqlite3\n\n'
    'conn = sqlite3.connect("habit.db")\n'
    'conn.commit()\n'
    'conn.close()\n\n'
    '# CREATE TABLE #\n\n'
    'import sqlite3\n\n'
    'conn = sqlite3.connect("habit.db")\n\n'
    'c = conn.cursor()\n'
    'c.execute("CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY, name TEXT)")\n'
    'conn.commit()\n'
    'conn.close()\n\n'
    '# INSERT ROW #\n\n'
    'import sqlite3\n\n'
    'conn = sqlite3.connect("habit.db")\n'
    'c = conn.cursor()\n'
    'c.execute("INSERT INTO fruits(name) VALUES(?)", ("apple",))\n'
    'conn.commit()\n'
    'conn.close()\n\n'
    '# READ DATA #\n\n'
    'import sqlite3\n\n'
    'conn = sqlite3.connect("habit.db")\n'
    'for row in conn.execute("SELECT * FROM fruits"):\n'
    '   print(row)\n'
    'conn.close()\n\n'
    '# DELETE DB #\n'
    'import os\n\n'
    'os.remove("habit.db")\n'
)

if not os.path.exists(sqlite3_cheatpath):
    with open(sqlite3_cheatpath, "w") as f:
        f.write(sqlite3_cheatcontent)

ollama_cheatpath = os.path.join(ollama_dir, "cheatsheet.md")
ollama_cheatcontent = (
    '# LIST OLLAMA MODELS #\n\n'
    'import ollama\n\n'
    'print(ollama.list())\n\n'
    '# FIRST OLLAMA PROMPT #\n\n'
    'import ollama\n\n'
    'response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": "Hello, World!"}])\n'
    'print(response["message"]["content"])\n\n'
    '# OLLAMA GENERATE PROMPT #\n\n'
    'import ollama\n\n'
    'result = ollama.generate(model="llama3.2", prompt="Explain what a CPU does in one sentence")\n'
    'print(result["response"])\n\n'
)

if not os.path.exists(ollama_cheatpath):
    with open(ollama_cheatpath, "w") as f:
        f.write(ollama_cheatcontent)

soup_cheatpath = os.path.join(soup_dir, "cheatsheet.md")
soup_cheatcontent = (
    '# PRETTIFY() #\n\n'
    'from bs4 import BeautifulSoup\n\n'
    'html = "<html><body><p>Hello, Friday!</p></body></html>"\n'
    'soup = BeautifulSoup(html, "html.parser")\n\n'
    'print(soup.prettify())\n\n'
    '# SELECT BY TAG #\n\n'
    'from bs4 import BeautifulSoup\n\n'
    'html = "<html><body><p>Hello Friday</p><p>How are you?</p></body></html>"\n'
    'soup = BeautifulSoup(html, "html.parser")\n\n'
    '# First <p> Tag\n'
    'print(soup.p)\n\n'
    '# Same Result\n'
    'print(soup.find("p"))\n\n'
    '# All <p> tags as a list\n'
    'print(soup.find_all("p"))\n\n\n'
    '# SELECT BY CLASS OR ID #\n\n'
    'from bs4 import BeautifulSoup\n\n'
    'html = <div class="note">Hi</div><div id="msg>Yo</div>"\n'
    'soup = BeautifulSoup(html, "html.parser")\n\n'
    'print(soup.find("div", class_="note"))\n'
    'print(soup.find("div", id="msg"))'
)

if not os.path.exists(soup_cheatpath):
    with open(soup_cheatpath, "w") as f:
        f.write(soup_cheatcontent)

print(f"Created daily folder structure for {today.strftime('%Y-%m%d')}")
