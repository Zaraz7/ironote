import sqlite3
from sqlite3 import Error

create_main_table = """
CREATE TABLE IF NOT EXISTS main (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  site TEXT NOT NULL,
  login TEXT NOT NULL,
  pass TEXT NOT NULL
);
"""

create_main_entry = """
INSERT INTO
  main (site, login, pass)
VALUES ("{}", "{}", "{}")
"""

create_vallue_main = """
INSERT INTO
  main (site, login, pass)
VALUES
  ('site - 1', 'male', 'USA'),
  ('Leila', 'female', 'France'),
  ('Brigitte', 'female', 'England'),
  ('Mike', 'male', 'Denmark'),
  ('Elizabeth', 'female', 'Canada');
"""

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return 'Error'

def create_bd(vallue = False, path = ''):

    connect = create_connection(path)

    execute_query(connect, create_main_table)
    execute_read_query(connect, create_main_entry.format("site", "login", "pass"))

    if vallue == True:
        execute_query(connect, create_vallue_main)