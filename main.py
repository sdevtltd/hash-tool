from core.hashing import *
from core.encoding import *
import os
import time

# ---------------- COLORS ----------------
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# ---------------- UTIL ----------------
def clear():
    os.system("clear")

def loading():
    print(Colors.GREEN + "Loading", end="")
    for i in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(Colors.RESET + "\n")

# ---------------- UI ----------------
def banner():
    logo = r"""
     _   _           _      _______           _
    | | | |         | |    |__   __|         | |
    | |_| | __ _ ___| |__     | | ___   ___ | |___
    |  _  |/ _` / __| '_ \    | |/ _ \ / _ \| / __|
    | | | | (_| \__ \ | | |   | | (_) | (_) | \__ \
    \_| |_/\__,_|___/_| |_|   |_|\___/ \___/|_|___/

            HASH TOOL TERMINAL
    """

    print(Colors.GREEN + logo + Colors.RESET)
    print(Colors.GREEN + "        Developed by SDev")
    print("        GitHub: https://github.com/sdevtltd")
    print("=" * 60 + Colors.RESET)

def menu():
    print("\n")
    print(f"{Colors.GREEN}[1]{Colors.RESET} Hash")
    print(f"{Colors.GREEN}[2]{Colors.RESET} Encode")
    print(f"{Colors.GREEN}[3]{Colors.RESET} Decode Base64")
    print(f"{Colors.GREEN}[4]{Colors.RESET} Exit")

# ---------------- MAIN ----------------
def main():
    while True:
        clear()
        banner()
        loading()
        menu()

        choice = input("\nSelect: ")

        if choice == "1":
            text = input("\nEnter text: ")
            print("\n" + Colors.GREEN + "--- RESULTS ---" + Colors.RESET)

            print(f"{Colors.GREEN}SHA1   :{Colors.RESET} {sha1(text)}")
            print(f"{Colors.GREEN}SHA256 :{Colors.RESET} {sha256(text)}")
            print(f"{Colors.GREEN}SHA512 :{Colors.RESET} {sha512(text)}")
            print(f"{Colors.GREEN}MD5    :{Colors.RESET} {md5(text)}")

            input("\nPress Enter...")

        elif choice == "2":
            text = input("\nEnter text: ")
            print("\n" + Colors.GREEN + "--- ENCODE ---" + Colors.RESET)

            print(f"{Colors.GREEN}Base16 :{Colors.RESET} {base16(text)}")
            print(f"{Colors.GREEN}Base32 :{Colors.RESET} {base32(text)}")
            print(f"{Colors.GREEN}Base64 :{Colors.RESET} {base64_encode(text)}")

            input("\nPress Enter...")

        elif choice == "3":
            text = input("\nEnter Base64: ")
            print("\n" + Colors.GREEN + "--- DECODE ---" + Colors.RESET)

            try:
                print(f"Decoded: {base64_decode(text)}")
            except:
                print(Colors.RED + "Invalid Base64" + Colors.RESET)

            input("\nPress Enter...")

        elif choice == "4":
            print("\nGoodbye 👋")
            print("Developed by SDev © 2026")
            break

        else:
            print(Colors.RED + "Invalid choice" + Colors.RESET)
            input("\nPress Enter...")

if __name__ == "__main__":
    main()
