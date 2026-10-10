# Rock Paper Scissors

A command-line Rock Paper Scissors game written in Python, where you play against the computer.

## Features

- The computer picks its move at random
- Handles all nine combinations of moves and announces a win, loss or tie
- Checks your input: entering text or a number other than 1–3 asks you again instead of crashing

## How to run

You need Python 3 installed.

```
python main.py
```

Then choose `1` for Rock, `2` for Paper or `3` for Scissors.

## What I learned

- Taking user input and converting it with `int()`
- Writing game logic with `if` / `elif` statements
- Generating random numbers with the `random` module
- Handling errors with `try` / `except` and repeating a prompt with a `while` loop
