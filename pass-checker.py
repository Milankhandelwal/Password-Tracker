# ...existing code...
import argparse
import re
import getpass
import sys

def show_banner() -> None:
    print(r"""
 ____                                _               ____ _               _             
|  _ \ __ _ ___ _____      _____  __| | ___  _ __   / ___| |__   ___  ___| | _____ _ __ 
| |_) / _` / __/ __\ \ /\ / / _ \/ _` |/ _ \| '__| | |   | '_ \ / _ \/ __| |/ / _ \ '__|
|  __/ (_| \__ \__ \\ V  V /  __/ (_| | (_) | |    | |___| | | |  __/ (__|   <  __/ |   
|_|   \__,_|___/___/ \_/\_/ \___|\__,_|\___/|_|     \____|_| |_|\___|\___|_|\_\___|_|   
                                                                                       
==========================================================================================
            Password Strength Checker - Learnex Internship
                Developed by: Milan Khandelwal 🔐
==========================================================================================
    """)

def check_password_strength(password: str):
    length_error = len(password) < 8
    lowercase_error = re.search(r'[a-z]', password) is None
    uppercase_error = re.search(r'[A-Z]', password) is None
    digit_error = re.search(r'\d', password) is None
    special_char_error = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    feedback = []
    if length_error: feedback.append("❌ Password must be at least 8 characters")
    if lowercase_error: feedback.append("❌ Add lowercase letters")
    if uppercase_error: feedback.append("❌ Add uppercase letters")
    if digit_error: feedback.append("❌ Add numbers")
    if special_char_error: feedback.append("❌ Add special characters (!@#$ etc.)")

    if score == 5:
        strength = "✅ Strong Password"
    elif 3 <= score < 5:
        strength = "⚠️ Moderate Password"
    else:
        strength = "🚫 Weak Password"

    return strength, feedback

def interactive_mode():
    try:
        password = getpass.getpass("🔑 Enter your password (input hidden): ")
    except Exception:
        # fallback if getpass fails (some IDEs/terminals)
        password = input("🔑 Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"\n🔎 Result: {strength}")
    for f in feedback:
        print(f)

def main():
    show_banner()

    parser = argparse.ArgumentParser(description="Password Strength Checker by Milan Khandelwal")
    parser.add_argument('--password', '-p', help='Password to analyze', type=str)

    args = parser.parse_args()

    if args.password:
        strength, feedback = check_password_strength(args.password)
        print(f"\n🔎 Result: {strength}")
        for f in feedback:
            print(f)
    else:
        print("\n🧠 No password provided via CLI. Switching to interactive mode...\n")
        interactive_mode()

if __name__ == "__main__":
    main()
# ...existing code...