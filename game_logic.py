import random

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """
    Select a random word from the predefined WORDS list.

    Returns:
        str: A randomly selected word.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
        Display the current game stage and return the formatted word progress.

        Args:
            mistakes (int): The number of incorrect guesses made so far.
            secret_word (str): The word the player is trying to guess.
            guessed_letters (list[str]): Letters that have already been
            guessed.

        Returns:
            str: A string representing the current progress of the word,
                 with guessed letters revealed and unguessed letters as
                 underscores.
    """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    return display_word


def play_game():
    """
        Run a single session of the Snowman Meltdown game.

        The function handles:
        - Selecting a random word
        - Processing user input
        - Tracking guesses and mistakes
        - Determining win/loss conditions

        Raises:
            ValueError: If the user inputs invalid data such as
            non-alphabetical
                        characters or more than one character at a time.
    """
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guess_letters = []
    max_mistakes = len(STAGES) - 1
    while True:
        print(display_game_state(mistakes, secret_word, guess_letters))
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if guess.isalpha():
            if guess in guess_letters:
                print("You already guessed that letter.")
                continue

            guess_letters.append(guess)

            if len(guess) > 1:
                raise ValueError(
                    "only a single alphabetical character is accepted")

            if guess in secret_word:
                print("Correct!")

            if guess not in secret_word:
                print("Wrong!")
                mistakes += 1

            if all(letter in guess_letters for letter in secret_word):
                print(f"Congratulations, you saved the snowman!")
                break

            if mistakes >= max_mistakes:
                print(STAGES[mistakes])
                print(f"Game Over! The word was {secret_word}")
                break
        else:
            raise ValueError("Only alphabets char are allowed")


def main():
    """
        Entry point for the Snowman Meltdown game.

        Handles:
        - Starting the game
        - Asking the user if they want to replay
        - Catching and displaying input-related errors

        Raises:
            ValueError: If the replay input is not 'y' or 'n'.
    """
    try:
        play_game()
        reply_option = input("Want to play again (y/n): ")
        if reply_option.lower() == "y":
            play_game()
        elif reply_option.lower() == "n":
            print("Goodbye! Hope you had fun.")
        else:
            raise ValueError("Please type (y) or (n)")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
