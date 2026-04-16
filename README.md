❄️ Snowman Meltdown (Python CLI Game)

A fun command-line word guessing game inspired by Hangman — but with a twist! Instead of a stick figure, your snowman slowly melts as you make mistakes.

🎮 How It Works
A random word is selected from a predefined list.
You guess one letter at a time.
Each wrong guess melts part of the snowman.
Guess the word before the snowman completely melts!
🧩 Features
Random word selection
ASCII art stages showing the snowman melting
Input validation with helpful error messages
Replay option after each game
Simple and beginner-friendly Python code
📂 Project Structure
.
├── main.py          # Main game logic
├── ascii_art.py     # Snowman melting stages (ASCII art)
└── README.md        # Project documentation
🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/snowman-meltdown.git
cd snowman-meltdown
2. Run the game
python main.py
🕹️ Gameplay Instructions
Run the program.
Enter a single letter when prompted.
Keep guessing until:
You guess the word correctly 🎉
OR the snowman melts completely ❌
⚠️ Rules
Only single alphabetical characters are allowed.
Repeated guesses are not counted but will prompt a warning.
Invalid input raises an error.
🧊 Example Words
python
git
github
snowman
meltdown
🔧 Possible Improvements
Add difficulty levels (easy, medium, hard)
Load words from a file or API
Add scoring system
Improve ASCII animations
Add multiplayer mode
🐛 Known Limitations
Game exits on invalid input instead of retrying
Word list is small and hardcoded
Case sensitivity is handled, but input must be valid