import argparse
import os

# Import algorithms
from algorithms.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
from algorithms.substitution import encrypt as subs_encrypt, decrypt as subs_decrypt


def read_file(path):
    """Reads the entire text from a file."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(path, data):
    """Writes the given text to a file."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)


def main():
    parser = argparse.ArgumentParser(
        description="Cryptix - Text Encryption and Decryption Tool"
    )

    # Required arguments
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

    # ===============================
    #       CAESAR CIPHER
    # ===============================
    if args.algo == "caesar":
        if args.shift is None:
            print("Error: --shift is required for Caesar Cipher")
            return

        if args.mode == "encrypt":
            result = caesar_encrypt(text, args.shift)
        else:
            result = caesar_decrypt(text, args.shift)

    # ===============================
    #    SUBSTITUTION CIPHER
    # ===============================
    elif args.algo == "substitution":
        if args.key is None or len(args.key) != 26:
            print("Error: Substitution Cipher requires a 26-letter key")
            return

        if args.mode == "encrypt":
            result = subs_encrypt(text, args.key)
        else:
            result = subs_decrypt(text, args.key)

    else:
        print("Unknown algorithm selected.")
        return

    # Save encrypted/decrypted output
    write_file(args.outfile, result)

    print(f"\nSuccess! Output saved to → {args.outfile}\n")
    print("CRYPTIX is now complete 🚀✨")


if __name__== "__main__":
    main()