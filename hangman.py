import random

# Predefined word list
WORDS = ["python", "hangman", "computer", "keyboard", "internet"]

# Hangman stages (0 = no mistakes, 6 = full hangman)
HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
    """
]

def get_display_word(word, guessed_letters):
    """Returns the word with unguessed letters replaced by underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("\n" + "="*40)
    print("       Welcome to HANGMAN!")
    print("="*40)
    print(f"The word has {len(word)} letters. You have {max_incorrect} incorrect guesses.\n")

    while incorrect_guesses < max_incorrect:
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Word: {get_display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        if guessed_letters:
            print(f"Letters guessed: {', '.join(sorted(guessed_letters))}")

        # Check if player has won
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word.upper())
            break

        # Get player input
        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")

    else:
        # Player ran out of guesses
        print(HANGMAN_STAGES[max_incorrect])
        print(f"\n💀 Game Over! The word was: {word.upper()}")

    # Ask to play again
    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again in ("yes", "y"):
        play_hangman()
    else:
        print("\nThanks for playing! Goodbye! 👋\n")

if __name__ == "__main__":
    play_hangman()