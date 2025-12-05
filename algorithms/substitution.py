
# algorithms/substitution.py
# Substitution Cipher for Cryptix
# Uses a 26-letter key to build encrypt/decrypt maps
# Then applies substitution_cipher() for both operations

import string

def substitution_cipher(text, substitution_alphabet):

    result = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            base_char = char.lower()
            substituted_char = substitution_alphabet.get(base_char, base_char)
            if is_upper:
                substituted_char = substituted_char.upper()
            result.append(substituted_char)
        else:
            result.append(char)
    return ''.join(result)

def build_map(key):

    key = key.lower()
    letters = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz

    encrypt_map = {letters[i]: key[i] for i in range(26)}
    decrypt_map = {key[i]: letters[i] for i in range(26)}

    return encrypt_map, decrypt_map

def encrypt(text, key):
    enc_map, _ = build_map(key)
    return substitution_cipher(text, enc_map)

def decrypt(text, key):
    _, dec_map = build_map(key)
    return substitution_cipher(text, dec_map)
