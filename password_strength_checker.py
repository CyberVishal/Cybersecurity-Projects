# trigger workflow test
# 🔐 Password Strength Checker
# Author: Your Name
# Description: Checks password strength based on length, characters, and complexity.

import re

def check_password_strength(password):
    # Scoring rules
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1
    
    # Contains lowercase, uppercase, numbers, and symbols
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Strength levels
    if strength <= 2:
        remarks = "Weak 🔴"
    elif strength == 3:
        remarks = "Moderate 🟡"
    elif strength >= 4:
        remarks = "Strong 🟢"

    return remarks

def main():
    password = input("Enter a password to test: ")
    result = check_password_strength(password)
    print(f"Password Strength: {result}")

if __name__ == "__main__":
    main()
