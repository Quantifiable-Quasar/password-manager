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
 - cleaning up the open/close functions 
    - they shouldn't be called as often as they are

