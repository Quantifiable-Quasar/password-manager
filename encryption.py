#!/usr/bin/env python3

from cryptography.fernet import Fernet

def generate_key(file):
    """
    This function generates a AES key 
    The file arg is just what you want to name the 
    file that the key will be stored in
    """
    key = Fernet.generate_key()

    with open(file, 'wb') as filekey:
        filekey.write(key)

def encrypt_file(keyfile, file_to_encrypt):
    with open(keyfile, 'rb') as file:
        key = file.read()

    fernet = Fernet(key)

    with open(file_to_encrypt, 'rb') as file:
        plaintext = file.read()

    cipher = fernet.encrypt(plaintext)

    with open(file_to_encrypt, 'wb') as encrypted_file:
        encrypted_file.write(cipher)

def decrypt_file(keyfile, file_to_decrypt):
    with open(keyfile, 'rb') as file:
        key = file.read()

    fernet = Fernet(key)
    
    with open(file_to_decrypt, 'rb') as encrypted_file:
        cipher = encrypted_file.read()

    decrypted = fernet.decrypt(cipher)

    return decrypted

print(decrypt_file('keyfile', 'test.txt'))
