# CREATE DB #

import sqlite3

conn = sqlite3.connect("habit.db")
conn.commit()
conn.close()

# CREATE TABLE #

import sqlite3

conn = sqlite3.connect("habit.db")

c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()
conn.close()

# INSERT ROW #

import sqlite3

conn = sqlite3.connect("habit.db")
c = conn.cursor()
c.execute("INSERT INTO fruits(name) VALUES(?)", ("apple",))
conn.commit()
conn.close()

# READ DATA #

import sqlite3

conn = sqlite3.connect("habit.db")
for row in conn.execute("SELECT * FROM fruits"):
   print(row)
conn.close()

# DELETE DB #
import os

os.remove("habit.db")
