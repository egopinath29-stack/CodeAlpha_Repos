"""
CodeAlpha - Task 1: Hangman Game
A simple text-based Hangman game.
"""

import random

# A small list of predefined words
WORDS = ["python", "hangman", "programming", "code", "alpha"]

MAX_WRONG_GUESSES = 6


def choose_word():
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(display_progress(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"🎉 You won! The word was '{word}'.")
            return

    print(f"💀 You lost! The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()
