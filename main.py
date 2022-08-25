#!/usr/bin/env python3

import sql_commands

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


