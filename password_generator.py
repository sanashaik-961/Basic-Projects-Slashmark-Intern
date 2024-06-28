import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 to ensure it includes all character types.")
        return None
    
    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password includes at least one of each character type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the generated password list to avoid predictable sequences
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    print("Welcome to the Python Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)
            if password:
                print(f"Generated password: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        play_again = input("Do you want to generate another password? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for using the password generator! Goodbye!")
            break

if __name__ == "__main__":
    main()
