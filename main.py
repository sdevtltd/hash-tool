from core.hashing import *
from core.encoding import *
import os
import time
import secrets
import string

# ---------------- COLORS ----------------
class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# ---------------- UTIL ----------------
def clear():
    os.system("clear")

def wait():
    input(Colors.YELLOW + "\nPress Enter..." + Colors.RESET)

def random_string(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

def loading():
    print(Colors.CYAN + "Loading", end="")
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
    """

    print(Colors.CYAN + Colors.BOLD + logo + Colors.RESET)
    print(Colors.GREEN + Colors.BOLD + "        HASH TOOL TERMINAL" + Colors.RESET)
    print(Colors.CYAN + "      Developed by SDev")
    print(Colors.CYAN + "      GitHub: https://github.com/sdevtltd")
    print(Colors.CYAN + "=" * 55 + Colors.RESET)

def menu():
    print("\n" + Colors.CYAN + "──────────── MENU ────────────" + Colors.RESET)

    print(f"{Colors.CYAN}[{Colors.YELLOW}1{Colors.CYAN}]{Colors.RESET} Hash")
    print(f"{Colors.CYAN}[{Colors.YELLOW}2{Colors.CYAN}]{Colors.RESET} Encode")
    print(f"{Colors.CYAN}[{Colors.YELLOW}3{Colors.CYAN}]{Colors.RESET} Decode Base64")
    print(f"{Colors.CYAN}[{Colors.YELLOW}4{Colors.CYAN}]{Colors.RESET} Random Hash")
    print(f"{Colors.CYAN}[{Colors.YELLOW}5{Colors.CYAN}]{Colors.RESET} Generate Token")
    print(f"{Colors.CYAN}[{Colors.YELLOW}6{Colors.CYAN}]{Colors.RESET} Exit")

# ---------------- MAIN ----------------
def main():
    while True:
        clear()
        banner()
        loading()
        menu()

        choice = input(Colors.YELLOW + "\nSelect: " + Colors.RESET)

        # ---------- HASH ----------
        if choice == "1":
            text = input(Colors.YELLOW + "\nEnter text: " + Colors.RESET)

            print("\n" + Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)
            print(Colors.CYAN + "        RESULTS" + Colors.RESET)
            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━\n" + Colors.RESET)

            print(f"{Colors.GREEN}SHA1   :{Colors.RESET} {sha1(text)}\n")
            print(f"{Colors.GREEN}SHA256 :{Colors.RESET} {sha256(text)}\n")
            print(f"{Colors.GREEN}SHA512 :{Colors.RESET} {sha512(text)}\n")
            print(f"{Colors.GREEN}MD5    :{Colors.RESET} {md5(text)}\n")

            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)

            wait()

        # ---------- ENCODE ----------
        elif choice == "2":
            text = input(Colors.YELLOW + "\nEnter text: " + Colors.RESET)

            print("\n" + Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)
            print(Colors.CYAN + "        ENCODE" + Colors.RESET)
            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━\n" + Colors.RESET)

            print(f"{Colors.GREEN}Base16 :{Colors.RESET} {base16(text)}\n")
            print(f"{Colors.GREEN}Base32 :{Colors.RESET} {base32(text)}\n")
            print(f"{Colors.GREEN}Base64 :{Colors.RESET} {base64_encode(text)}\n")

            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)

            wait()

        # ---------- DECODE ----------
        elif choice == "3":
            text = input(Colors.YELLOW + "\nEnter Base64: " + Colors.RESET)

            print("\n" + Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)
            print(Colors.CYAN + "        DECODE" + Colors.RESET)
            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━\n" + Colors.RESET)

            try:
                print(f"{Colors.GREEN}Decoded :{Colors.RESET} {base64_decode(text)}")
            except:
                print(Colors.RED + "Invalid Base64" + Colors.RESET)

            print("\n" + Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)

            wait()

        # ---------- RANDOM HASH ----------
        elif choice == "4":
            text = random_string()

            print("\n" + Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)
            print(Colors.CYAN + "     RANDOM INPUT" + Colors.RESET)
            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━\n" + Colors.RESET)

            print(text)

            print("\n" + Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)
            print(Colors.CYAN + "      HASH RESULTS" + Colors.RESET)
            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━\n" + Colors.RESET)

            print(f"{Colors.GREEN}SHA1   :{Colors.RESET} {sha1(text)}\n")
            print(f"{Colors.GREEN}SHA256 :{Colors.RESET} {sha256(text)}\n")
            print(f"{Colors.GREEN}SHA512 :{Colors.RESET} {sha512(text)}\n")
            print(f"{Colors.GREEN}MD5    :{Colors.RESET} {md5(text)}\n")

            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)

            wait()

        # ---------- TOKEN ----------
        elif choice == "5":
            token = secrets.token_urlsafe(32)

            print("\n" + Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)
            print(Colors.CYAN + "   GENERATED TOKEN" + Colors.RESET)
            print(Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━\n" + Colors.RESET)

            print(Colors.GREEN + token + Colors.RESET)

            print("\n" + Colors.CYAN + "━━━━━━━━━━━━━━━━━━━━━━" + Colors.RESET)

            wait()

        # ---------- EXIT ----------
        elif choice == "6":
            print("\n" + Colors.GREEN + "Goodbye 👋" + Colors.RESET)
            print(Colors.CYAN + "Developed by SDev © 2026" + Colors.RESET)
            break

        # ---------- INVALID ----------
        else:
            print(Colors.RED + "Invalid choice" + Colors.RESET)
            wait()

if __name__ == "__main__":
    main()
