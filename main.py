from core.hashing import *
from core.encoding import *
import os

def clear():
    os.system("clear")

def header():
    print("=" * 40)
    print("        🔐 HASH TOOL TERMINAL")
    print("=" * 40)

def menu():
    print("\n[1] Hash")
    print("[2] Encode")
    print("[3] Decode Base64")
    print("[4] Exit")

def main():
    while True:
        clear()
        header()
        menu()

        choice = input("\nSelect: ")

        if choice == "1":
            text = input("\nEnter text: ")
            print("\n--- RESULTS ---")
            print("SHA1   :", sha1(text))
            print("SHA256 :", sha256(text))
            print("SHA512 :", sha512(text))
            print("MD5    :", md5(text))
            input("\nPress Enter...")

        elif choice == "2":
            text = input("\nEnter text: ")
            print("\n--- ENCODE ---")
            print("Base16 :", base16(text))
            print("Base32 :", base32(text))
            print("Base64 :", base64_encode(text))
            input("\nPress Enter...")

        elif choice == "3":
            text = input("\nEnter Base64: ")
            try:
                print("Decoded:", base64_decode(text))
            except:
                print("Invalid Base64")
            input("\nPress Enter...")

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")
            input("\nPress Enter...")

if __name__ == "__main__":
    main()
