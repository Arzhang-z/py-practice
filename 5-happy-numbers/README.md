# Happy Number Checker

This project provides a simple Python implementation to check whether a given number is a **happy number**.

## What is a Happy Number?
A **happy number** is defined by the following process:

1. Start with any positive integer.
2. Replace the number with the sum of the squares of its digits.
3. Repeat the process until:
   - The number becomes `1` (the number is happy), or
   - The process enters a loop that does not include `1` (the number is not happy).

## Example
- `19 → 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1` → **Happy**
- `2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4` (loop) → **Not Happy**

## Features
- Efficient cycle detection using a `set`
- Clear function documentation with doctests
- Interactive command-line interface
- Simple and readable implementation

## Code Overview
The core logic is implemented in the function:

```python
def is_happy(n: int) -> bool:
```

The function tracks previously seen numbers to detect infinite loops and stops when either `1` is reached or a cycle is detected.

## Usage

### Run the Script

```bash
python happy_number.py
```

### Interactive Mode
Once running, you can enter numbers to check whether they are happy:

```text
Enter a number and check if it is a happy number (press 'q' to exit):
```

Type `q` to quit the program.

### Example Output

```text
44 is a happy number!
45 is not a happy number
```

## Tests
Basic assertions are included in the `__main__` block:

```python
assert is_happy(7) is True
assert is_happy(45) is False
assert is_happy(44) is True
```

These help verify correctness during execution.

## Requirements
- Python 3.9 or higher (for type hints like `set[int]`)

## Possible Improvements
- Input validation for non-integer values
- Performance optimization using Floyd’s cycle detection algorithm
- Unit tests using `pytest`
- Packaging as a reusable module

## License
This project is free to use for educational and personal purposes.

