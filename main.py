#!/usr/bin/env python3

import sql
import encryption
import sys
import hashlib
import getpass

print("I hid the password. Just trust that it is getting recorded.")

def check_pass():
    try:
        with open('masterpass.txt', 'rb') as file:
            master_pass = file.read()
    except:
        print("You are missing a master pass file.")
        print("You need to re-run the program with the -new flag")
        sys.exit() 
    for i in range(3):
        user_password = getpass.getpass("Enter the master password ")
        if hashlib.sha512(user_password.encode('UTF-8')).hexdigest() == master_pass.decode('UTF-8'):
            return True
            break
        else:
            print("Incorrect Password!")

if '-new' in sys.argv: 
    new_master_pass = getpass.getpass("What do you want to be the master pass? ")
    verify = getpass.getpass("Type that in again. If you loose this the db is gonzo ")
    if new_master_pass == verify:
        with open('masterpass.txt', 'wb') as file:
            file.write(hashlib.sha512(new_master_pass.encode("UTF-8")).hexdigest())
    else:
        print("""   Good thing I saved you there with that extra check! 
        You couldn't even remeber the password for 5 seconds.
        That database would have been gonzo
        Not like Anthony Gonzolez either. 
        It would have just been bad.
        Luckily for you I added an extra check in there!""")
    
    exit

if not check_pass():
    exit

while True:
    print('\n'+50*'=')
    print('Password Manager Main Menu')
    print(50*'=')
    function_selection = input("What would you like to do? ").upper().strip()
    if function_selection not in ['C', 'R', 'U', 'D', 'Q', 'CREATE', 'READ', 'UPDATE', 'DELETE', 'QUIT']:
        print("""Invalid option. Please select one of the CRUD operations.
                C/CREATE:   Create a new entry into the db
                R/READ:     Print an existing entry in the db
                U/UPSDATE:  Update an existing entry in the db
                D/DELETE:   Delete an entry from the db
                Q/QUIT:     Quit this program""")

    elif function_selection in ['C', 'CREATE']:
       sql_commands.create()
    elif function_selection in ['R', 'READ']:
        sql_commands.read()
    elif function_selection in ['U', 'UPDATE']:
        sql_commands.update()
    elif function_selection in ['D', 'DELETE']:
        sql_commands.delete()
    elif function_selection in ['Q', 'QUIT']:
        sql_commands.close_db()
        break


