import random

def display_welcome():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it and I'll give you hints along the way.")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_guess(guess, target):
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number correctly!")
        return True
    return False

def play_game():
    target_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        if check_guess(guess, target_number):
            break
    print(f"You guessed the number in {attempts} attempts!")

def main():
    display_welcome()
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
