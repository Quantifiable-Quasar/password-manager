# password-manager
This is a python password manager tool.

# This project is more thouroughly documented
[Click Here](https://quantifiable-quasar.com/?p=13)

## Backend
This is written in python, and uses a SQL database for persistence.
I chose to use sqlite3 because it came built in with python.
Right now the tool supports basic CRUD operations.
Techinically it does work as a password manager, but I would recoment finding a better option.
As of now the database is horribly unencrypted, and the passwords are recoverable just by viewing the file.

## What's next for the project?

 - Fixing the password generator
 - encrypting the file with an AES key
 - Adding password authentication 
    - store hashed/salted pass and check against user input
 - cleaning up the open/close functions 
    - they shouldn't be called as often as they are


### Random notes for me
file = open('pass.db')
conn = sql.open(file)

That way you could decrypt locally without writting the decrypted file to disk
This may be the decryption solution!
