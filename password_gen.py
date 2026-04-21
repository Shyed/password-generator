# Import modules for random selection and character sets
import random
import string

# Generate a random password based on user options
def generate_password(length, use_uppercase=True, use_numbers=True, use_specials=True):
    # Start with lowercase letters
    characters = list(string.ascii_lowercase)

    # Add character sets based on user choices
    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_numbers:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()_+-=[]{}|;:,.<>?")

    # Ensure character pool is not empty
    if not characters:
        raise ValueError("No character types selected for password.")

    # Generate password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Main CLI program
if __name__ == "__main__":
    print("=== Password Generator ===")

    try:
        # Get user input
        length = int(input("Enter password length: "))
        include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_specials = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate password
        pwd = generate_password(length, include_upper, include_numbers, include_specials)

        # Display result
        print("\nGenerated password:")
        print(pwd)

    # Handle invalid input
    except ValueError as ve:
        print("Error:", ve)
