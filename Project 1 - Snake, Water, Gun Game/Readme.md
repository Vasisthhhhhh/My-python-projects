# Snake, Water, Gun Game

This is a Python implementation of the classic **Snake, Water, Gun** game. The game is similar to Rock, Paper, Scissors, where each option can defeat or lose to another option based on predefined rules.

## How to Play

1. Run the Python script `main.py`.
2. Enter your choice:
   - `S` for Snake
   - `W` for Water
   - `G` for Gun
3. The computer will randomly choose one of the three options.
4. The game will display the choices and the result:
   - **Draw**: Both the player and the computer chose the same option.
   - **Win**: Your choice defeats the computer's choice.
   - **Lose**: The computer's choice defeats your choice.

## Rules

- **Snake** defeats **Water** but loses to **Gun**.
- **Water** defeats **Gun** but loses to **Snake**.
- **Gun** defeats **Snake** but loses to **Water**.

-------------------------------------------------------------------------------

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the `main.py` file.
2. Open a terminal and navigate to the directory containing `main.py`.
3. Run the script using the command:

   ```sh
   python main.py
