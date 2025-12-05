# Cryptix

A text Encryption and Decryption tool designed to demonstrate classical cryptography algorihms, featuring both a command-line interface and an interactive menu system.
This project wa dveloped as part of the CS433-Comuter Security Course at Taibah University, Completed by Group 2.

Cryptix allows users to encrypt and decrypt text using two classical cryptographic algorithms:

 • Caesar Cipher
 • Substitution Cipher

The tool supports:
 • Manual text input
 • File-based input
 • Custom keys and shift values
 • Saving output into text files

# Project Structure
 Cryptix/
 ├── algorithms/
 │     ├── caesar.py
 │     └── substitution.py
 ├── tests/
 │     ├── caesar_tests
 │     └── substitution_tests
 ├── samples/
 ├── main.py
 ├── README.md
 └── logo.jpg
# Algorithms Used
1. Caesar Cipher

A classical substitution cipher that shifts letters by a fixed number (key).
Simple, predictable, and widely used in introductory cryptography.

Example (Shift = 4): HELLO --> LIPPS

2. Substitution Cipher

Each letter is replaced by another letter based on a 26-character key.
More secure than Caesar because it does not follow a simple pattern.

Example Key: PHQGIUMEAYLNOFDXJKRCVSTZWB

# Usage
1.Interactive Mode

Run: python main.py
The tool will guide you through:
 • Choosing algorithm
 • Selecting mode (encrypt / decrypt)
 • Entering shift/key
 • Choosing input type (manual or file)
 • Saving output (optional)

 2.CLI Mode 

 Caesar Encrypt: 
 python main.py --algo caesar --mode encrypt --infile samples/input.txt --outfile samples/enc.txt --shift 3
 Caesar Decrypt:
 python main.py --algo caesar --mode decrypt --infile samples/enc.txt --outfile samples/dec.txt --shift 3
 Substitution Encrypt:
 python main.py --algo substitution --mode encrypt --infile samples/input.txt --outfile samples/enc.txt --key PHQGIUMEAYLNOFDXJKRCVSTZWB
 Substitution Decrypt:
 python main.py --algo substitution --mode decrypt --infile samples/enc.txt --outfile samples/dec.txt --key PHQGIUMEAYLNOFDXJKRCVSTZWB

 # Libaries Used
 1. argparse

Used to build the command-line interface (CLI).
It allows the tool to read user arguments such as algorithm name, mode, key, input file, and output file.

2. os

Used to check file availability and interact with the file system.
This prevents errors when users enter incorrect file paths.

3. sys

Used to detect whether the tool was launched with arguments or without them.
This enables switching between CLI mode and Interactive Menu mode.

# Cryptix Team
1.Amnah Abdullah Mukhtar
2.
3.
4.
5.

