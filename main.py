import argparse
import os
import sys

# Import algorithms
from algorithms.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
from algorithms.substitution import encrypt as subs_encrypt, decrypt as subs_decrypt


def read_file(path):
    """Reads the text from a file."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(path, data):
    """Writes the given text to a file."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)


def interactive_menu():
    print("\n Welecome to Cryptix")
    print("===========================\n")

    # Select algorithm
    print("Choose Algorithm:")
    print("1) Caesar Cipher")
    print("2) Substitution Cipher")
    algo_choice = input("Enter choice (1 or 2): ")

    if algo_choice == "1":
        algo = "caesar"
    elif algo_choice == "2":
        algo = "substitution"
    else:
        print("Invalid choice.")
        return

    # Select mode
    print("\nChoose Mode:")
    print("1) Encrypt")
    print("2) Decrypt")
    mode_choice = input("Enter choice (1 or 2): ")

    if mode_choice == "1":
        mode = "encrypt"
    elif mode_choice == "2":
        mode = "decrypt"
    else:
        print("Invalid mode.")
        return

    # Algorithm input
    shift = None
    key = None

    if algo == "caesar":
        shift = int(input("\nEnter shift number: "))

    elif algo == "substitution":
        key = input("\nEnter 26-letter substitution key: ")
        if len(key) != 26:
            print("Key must be exactly 26 letters.")
            return

    # Choose input method
    print("\nChoose input method:")
    print("1) Enter text")
    print("2) Read from file")
    input_choice = input("Enter choice (1 or 2): ")

    if input_choice == "1":
        text = input("\nEnter your text: ")

    elif input_choice == "2":
        infile = input("\nEnter input file path: ")
        text = read_file(infile)

    else:
        print("Invalid choice.")
        return

    # Execute algorithm
    if algo == "caesar":
        result = caesar_encrypt(text, shift) if mode == "encrypt" else caesar_decrypt(text, shift)

    else:  # substitution
        result = subs_encrypt(text, key) if mode == "encrypt" else subs_decrypt(text, key)

    # Show result
    print("Result")
    print(result)
    print("================================================\n")

    # Ask to save output
    save = input("Do you want to save the result to a file? (y/n): ")

    if save.lower() == "y":
        outfile = input("Enter output file path: ")
        write_file(outfile, result)
        print(f"\n✨ Output saved successfully to: {outfile}\n")
    else:
        print("\nResult not saved.\n")



#       COMMAND-LINE MODE
def main():
    parser = argparse.ArgumentParser(
        description="Cryptix - Text Encryption and Decryption Tool"
    )

    parser.add_argument("--algo", required=True,
                        choices=["caesar", "substitution"],
                        help="Choose the encryption algorithm")

    parser.add_argument("--mode", required=True,
                        choices=["encrypt", "decrypt"],
                        help="Choose operation mode")

    parser.add_argument("--infile", required=True,
                        help="Path to input file")

    parser.add_argument("--outfile", required=True,
                        help="Path to save output")

    # Optional values
    parser.add_argument("--shift", type=int,
                        help="Shift value for Caesar Cipher")

    parser.add_argument("--key",
                        help="26-letter key for Substitution Cipher")

    args = parser.parse_args()

    # Check input file existence
    if not os.path.exists(args.infile):
        print("Error: Input file not found.")
        return

    # Read input text
    text = read_file(args.infile)

    
    #CAESAR CIPHER
    
    if args.algo == "caesar":
        if args.shift is None:
            print("Error: --shift is required for Caesar Cipher")
            return

        result = caesar_encrypt(text, args.shift) if args.mode == "encrypt" else caesar_decrypt(text, args.shift)

    #SUBSTITUTION CIPHER

    elif args.algo == "substitution":
        if args.key is None or len(args.key) != 26:
            print("Error: Substitution Cipher requires a 26-letter key")
            return

        result = subs_encrypt(text, args.key) if args.mode == "encrypt" else subs_decrypt(text, args.key)

    write_file(args.outfile, result)
    print(f"\nSuccess! Output saved to → {args.outfile}\n")
    print("CRYPTIX is now complete 🚀✨")



if __name__=="__main__":
    # If the user runs python main.py with NO arguments → open menu mode
    if len(sys.argv) == 1:
        interactive_menu()
    else:
        main() 
