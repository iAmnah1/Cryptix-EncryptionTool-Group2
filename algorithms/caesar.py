
# algorithms/caesar.py

import string

def encrypt(text, key):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            original_position = alphabet.index(letter)
            new_position = (original_position + key) % 26
            new_letter = alphabet[new_position]
            if letter.isupper():
                encrypted_text += new_letter.upper()
            else:
                encrypted_text += new_letter
        else:
            encrypted_text += letter
    return encrypted_text

def decrypt(text, key):
    return encrypt(text, -key)
