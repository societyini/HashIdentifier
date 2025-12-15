import os
import time
import re

# =========================
# COLORES
# =========================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# =========================
# BANNER
# =========================
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Colors.CYAN}{Colors.BOLD}
 ██╗  ██╗ █████╗ ███████╗██╗  ██╗
 ██║  ██║██╔══██╗██╔════╝██║  ██║
 ███████║███████║███████╗███████║
 ██╔══██║██╔══██║╚════██║██╔══██║
 ██║  ██║██║  ██║███████║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

            SOCIETY.INI
           Hash Identifier
        discord.gg/7ZHueg8gWZ
{Colors.RESET}""")

# =========================
# IDENTIFICADOR
# =========================
def identify_hash(hash_value):
    hash_value = hash_value.strip()

    patterns = {
        "MD5": r"^[a-fA-F0-9]{32}$",
        "SHA1": r"^[a-fA-F0-9]{40}$",
        "SHA256": r"^[a-fA-F0-9]{64}$",
        "SHA512": r"^[a-fA-F0-9]{128}$",
        "NTLM": r"^[a-fA-F0-9]{32}$",
        "MySQL (old)": r"^[a-fA-F0-9]{16}$",
    }

    matches = []

    for name, pattern in patterns.items():
        if re.match(pattern, hash_value):
            matches.append(name)

    return matches

# =========================
# MAIN
# =========================
def main():
    while True:
        banner()

        hash_input = input(f"{Colors.YELLOW}Introduce el hash: {Colors.RESET}")

        if hash_input.strip() == "":
            print(f"{Colors.RED}El hash no puede estar vacío.{Colors.RESET}")
            time.sleep(1.5)
            continue

        results = identify_hash(hash_input)

        print(f"\n{Colors.GREEN}{Colors.BOLD}Posibles tipos de hash:{Colors.RESET}\n")

        if results:
            for r in results:
                print(f"{Colors.CYAN}- {r}{Colors.RESET}")
        else:
            print(f"{Colors.RED}No se pudo identificar el tipo de hash.{Colors.RESET}")

        choice = input(
            f"\n{Colors.YELLOW}¿Quieres identificar otro hash? (s/n): {Colors.RESET}"
        ).lower()

        if choice != "s":
            print(f"\n{Colors.BOLD}Proceso finalizado.{Colors.RESET}")
            break

# =========================
# START
# =========================
if __name__ == "__main__":
    main()
