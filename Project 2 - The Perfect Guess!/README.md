


# The Perfect Guess!

This is a Python-based number guessing game where the user tries to guess a randomly generated number between 1 and 99. The game provides feedback on whether the guess is too high, too low, or correct. The user can also exit the game at any time.

## How to Play

1. Run the `main.py` file to start the game.
2. The program will generate a random number between 1 and 99.
3. Enter your guess when prompted.
4. The program will provide feedback:
   - **Too low**: Your guess is lower than the target number.
   - **Too high**: Your guess is higher than the target number.
   - **Correct**: You guessed the number correctly!
5. You can exit the game by entering `-1`.

## Features

- Random number generation using Python's `random` module.
- Feedback for each guess.
- Keeps track of the number of guesses.
- Option to exit the game at any time.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the project files.
2. Navigate to the `Project 2 - The Perfect Guess!` directory.
3. Run the following command in your terminal:

   ```bash
   python main.py


-------------------------------------------------------------------------------------------------------------------------------

#Example Output

Guess a number between 1 and 99 (or -1 to exit): 
50
Too low, try again!

Guess a number between 1 and 99 (or -1 to exit): 
75
Too high, try again!

Guess a number between 1 and 99 (or -1 to exit): 
60
WOHOO! Congratulations, You guessed it right in 3 guesses!
