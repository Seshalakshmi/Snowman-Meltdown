from game_logic import play_game

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

    play_game()
    while True:
        try:
            reply_option = input("Want to play again (y/n): ")
            if reply_option.lower() == "y":
                play_game()
                continue
            elif reply_option.lower() == "n":
                print("Goodbye! Hope you had fun.")
                break
            else:
                raise ValueError("Please type (y) or (n)")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()