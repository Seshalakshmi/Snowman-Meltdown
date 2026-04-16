import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    return display_word


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guess_letters = []
    max_mistakes = len(STAGES) - 1
    while True:
        print(display_game_state(mistakes, secret_word, guess_letters))
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in guess_letters:
            print("You already guessed that letter.")
            continue

        guess_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

        if all(letter in guess_letters for letter in secret_word):
            print(f"Congratulations, you saved the snowman!")
            break

        if mistakes >= max_mistakes:
            print(STAGES[mistakes])
            print(f"Game Over! The word was {secret_word}")
            break


if __name__ == "__main__":
    play_game()