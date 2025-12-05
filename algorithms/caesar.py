
# algorithms/caesar.py

import string

def encrypt(plaintext, key):
    alphabet = string.ascii_lowercase
    encrypted_word = ""
    for letter in plaintext:
        if letter in alphabet:
            original_position = alphabet.index(letter)
            new_position = (original_position + key) % 26
            new_letter = alphabet[new_position]
            if letter.isupper():
                encrypted_word += new_letter.upper()
            else:
                encrypted_word += new_letter
        else:
            encrypted_word += letter
    return encrypted_word

def decrypt(plaintext, key):
    return encrypt(plaintext, -key)
