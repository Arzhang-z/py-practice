# Password Generator tool

this project is a python based dashboard tool for making a unique code using three methods.
1. method `Pin Generator` gets the length from user and generates pin code, 
2. method `Random Password Generator` gets length, and asks the user if he wants to add numbers and symbols then generates the password
3. method `Memorable Password Generator` gets number of words, seperator, Capitalization and vocabulary in order to choose words from them and make the password, but if the vocabulary arg is None, it uses nltk library to use its word.


## File structure

password-genrator/
|
|-- src/
|   |
|   |-- mian.ipynb
|   |-- main.py
|
|-- tests.py
|-- requirements.txt
|-- README.md



## Requirements
1. python 3.6+: This project uses several Python 3.6+ features like fstrings and type hinting
2. nltk==3.9.2: natural-language-tool-kit is a library that keeps a large cale of words inside it, and we did use it to gather words in order to make words in `Memorable Password Generator` method.

To install the requirements:

```bash
pip install -r requirements.txt
```

## How to Run
To run the project

```python
python src/main.py
```
this file can be opened by running the `main.py` script.