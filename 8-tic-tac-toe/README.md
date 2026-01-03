# Tic Tac Toe – Python CLI Game

A simple, interactive Tic Tac Toe game for two players, playable from the command line. Features input validation, win/draw detection, random first player selection, and replay functionality.

## Features

- Two-player gameplay (X and O)

- Randomized first player for fairness

- Input validation for numbers (1–9) and preventing moves on occupied cells

- Automatic win detection (rows, columns, diagonals)

- Detects draw games when the board is full

- Replay option without restarting the program

- Pure Python, no external dependencies

## Requirements

-Python 3.9+

## Installation

Clone the repository:

```bash
git clone https://github.com/Arzhang-z/py-prcatice/8-tic-tac-toe.git
```

Navigate to the folder:

```bash
cd 8-tic-tac-toe
```

Run the game:

```bash
python tic_tac_toe.py
```
## How to Play

- Players take turns entering a number from 1 to 9 to place their mark (X or O) on the board.

Board positions:
```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

- The first player is chosen randomly.

- Invalid or occupied inputs prompt the player to try again.

- The game ends when a player wins or the board is full (draw).

- Players can choose to play again at the end.

## Project Structure
```
tic-tac-toe/
├── tic_tac_toe.py      # Main Python script
└── README.md           # Project documentation
```

## License

Free to use, modify, and share for learning and personal projects.