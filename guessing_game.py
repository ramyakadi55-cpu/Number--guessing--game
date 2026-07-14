"""
Number Guessing Game
A simple CLI game where the player tries to guess a random number.
"""

import random


def play_game():
    print("=" * 40)
    print("  Welcome to the Number Guessing Game!")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")

        if not guess_input.isdigit():
            print("Please enter a valid number.\n")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"\n🎉 Correct! You guessed it in {attempts} attempt(s)!")
            return

    print(f"\nGame over! The number was {secret_number}. Better luck next time!")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break
        print()


if __name__ == "__main__":
    main()
