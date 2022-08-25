#!/usr/bin/env python3

import sqlite3
import password_generator


def open_db():
    global c
    global conn

    # Establish connection to sqlite database
    conn = sqlite3.connect('password.db')
    c = conn.cursor()

    # Create table if db does not exist
    c.execute("""CREATE TABLE IF NOT EXISTS passwords (
        id integer PRIMARY KEY,
        service text NOT NULL,
        username text,
        password text,
        url text
        );""")

def close_db():
    conn.close()

open_db()
close_db()

def create():
    open_db()
    c.execute("SELECT * FROM passwords ORDER BY id DESC LIMIT 1;")
    largest_id = c.fetchone()
    try:
        new_id = largest_id[0] + 1
    except:
        new_id = 1
    new_service = input("Title of entry: ")
    new_username = input("Username: ")
    new_password = input("Password: (* for random) ")
    new_url = input("URL: ")
    
    if new_password == "*":
        new_password = password_generator.pw_gen() 

    c.execute("INSERT INTO passwords VALUES (?, ?, ?, ?, ?)", (new_id, new_service, new_username, new_password, new_url))
    conn.commit()
    close_db()

def read(entry=None):
    open_db()
    if not entry:
        entry = input("Which entry to observe: ")
    print("="*50)
    try: 
        dump = c.execute("SELECT * FROM passwords WHERE service = ?", (entry,)).fetchone()
        print("""Entry {}
        Service: {}
        Username: {}
        Password: {}
        Url: {}""".format(dump[0], dump[1], dump[2], dump[3], dump[4]))
    except:
        print("Invlaid input. Options are: ")
        entries = c.execute("SELECT service FROM passwords").fetchall()
        for i in entries:
            print("    -" + i[0])
    close_db()

def update():
    open_db()
    columns = [ i[0] for i in c.execute("SELECT * FROM passwords").description ]

    print("Entries are: ")
    entries = c.execute("SELECT service FROM passwords;").fetchall()
    for i in entries:
        print("    -" + i[0])
    entry_to_update = input("Which entry to update? ") 
    read(entry_to_update)
    open_db()
    try:
        index_to_update = c.execute("SELECT id FROM passwords WHERE service = ?", (entry_to_update,)).fetchone()[0]
    except:
        print("Error restarting function")
        close_db()
        update()

    field_to_update = input("Select field to update: ").lower().strip()
    updated_value = input("Enter new value: ")
    if field_to_update not in columns or field_to_update == "id":
        print("Invalid option")
        print("Choose from", columns[1:])
        update()
    if field_to_update == 'url':
        c.execute("UPDATE passwords SET 'url' = ? WHERE id = ?", (updated_value, index_to_update)) 
    if field_to_update == 'service':
        c.execute("UPDATE passwords SET 'service' = ? WHERE id = ?", (updated_value, index_to_update)) 
    if field_to_update == 'password':
        c.execute("UPDATE passwords SET 'password' = ? WHERE id = ?", (updated_value, index_to_update)) 
    if field_to_update == 'username':
        c.execute("UPDATE passwords SET 'username' = ? WHERE id = ?", (updated_value, index_to_update)) 
    conn.commit()
    close_db()

def delete():
    print("*"*50)
    print("WARNING YOU ARE ABOUT TO PERMANATELY DELETE AN ENTRY")
    print("*"*50)

    entry_to_delete = input("Which entry would you like to permanetly delete? ")
    read(entry_to_delete)
    open_db()
    if input("Are you sure you want to delte this entry? [Y/N]") == 'Y':
        c.execute("DELETE FROM passwords WHERE service = ?", (entry_to_delete,))
    conn.commit()
    close_db()
