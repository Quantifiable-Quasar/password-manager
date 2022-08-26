#!/usr/bin/env python3

from cryptography.fernet import Fernet
from os.path import exists

def generate_key():
    """
    This function generates a AES key 
    The file arg is just what you want to name the 
    file that the key will be stored in
    """
    key = Fernet.generate_key()
    if exists('aes.key'):
        print("Error: Key File already exists")
        exit 

    with open('aes.key', 'wb') as filekey:
        filekey.write(key)

def encrypt_file(file_to_encrypt):
    with open('aes.key', 'rb') as file:
        key = file.read()

    fernet = Fernet(key)

    with open(file_to_encrypt, 'rb') as file:
        plaintext = file.read()

    cipher = fernet.encrypt(plaintext)

    with open(file_to_encrypt, 'wb') as encrypted_file:
        encrypted_file.write(cipher)

def decrypt_file(file_to_decrypt):
    with open('aes.key', 'rb') as file:
        key = file.read()

    fernet = Fernet(key)
    
    with open(file_to_decrypt, 'rb') as encrypted_file:
        cipher = encrypted_file.read()

    decrypted = fernet.decrypt(cipher)

    #return decrypted
    with open(file_to_decrypt, 'wb') as file:
        file.write(decrypted)
