import random
import string

# Developer note: Main function to generate the password
def generate_password(length, use_uppercase=True, use_numbers=True, use_specials=True):
    # Developer note: Start with lowercase letters by default
    characters = list(string.ascii_lowercase)

    # Developer note: Add character sets based on user input
    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_numbers:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()_+-=[]{}|;:,.<>?")

    # Developer note: Check if character pool is valid
    if not characters:
        raise ValueError("No character types selected for password.")

    # Developer note: Randomly generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Developer note: CLI user input and execution
if __name__ == "__main__":
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_specials = input("Include special characters? (y/n): ").lower() == 'y'

        pwd = generate_password(length, include_upper, include_numbers, include_specials)
        print("\nGenerated password:")
        print(pwd)
    except ValueError as ve:
        print("Error:", ve)
