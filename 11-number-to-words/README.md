# Number To Word Project
This is a CLI python-based project that gets a number from user and returns the word-representation of it
#### Note: This function only works for numbers less than 10^15 and equal or greater than 0

## Project Structure

```
.
├── src/
├   ├── main.py # main cli project 
├   ├── constants.py # word container logic
├   ├── test.ipynb # includes traingn for recursive func
├
├ dependencies
└── README.md # Project documentation
```

## Features
- built in assertation that checks if the logic works fluently
- recursive function example
- User can Enter multiple numbers without wnating to run it again
- checks User input without getting Error

## Dependencies
- `Python`3.7+ : this project uses multiple methods like fstrings that requires Python 3.7 or higher

## How to Run
fisrt open the code directory with:
```bash
cd 11-num-to-words
```
then export project file location inorder to be able to use dependencies:
```bash
export PYTHONPATH=$PYTHONPATH:(cwd)
```
Then simply run the project like:
```bash
python src/main.py
```


then it gets a number from user and returns the word representation of it, and check if user wants to enter another number


