import string
from src.main import RandomPaswordGenerator
from src.main import MemorablePasswordGenerator
from src.main import PinGenerator

import nltk

nltk.download("words")


def test_random_password_genartor():
    random_gen = RandomPaswordGenerator(length=10, include_numbers=True,include_symbols=True)
    password = random_gen.generate()
    print(password)
    assert len(password) == 10
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)


def test_memorable_password_generator():
    memorable_gen = MemorablePasswordGenerator(
        number_of_words=4,
        seperator="_",
        capitalization=True,
        vocabulary=nltk.corpus.words.words()
    )
    password = memorable_gen.generate()
    print(password)
    assert len(password.split("_")) == 4
    assert any(word[0].isupper() for word in password.split("_"))


def test_pincode_generator():
    pin_gen = PinGenerator(8)
    pin = pin_gen.generate()
    print(pin)
    assert len(pin) == 8
    assert all(char in string.digits for char in pin)


def main():
    print("Testing RandomPasswordGenerator:")
    test_random_password_genartor()
    print("Testing MemorablePasswordGenerator:")
    test_memorable_password_generator()
    print("Testing PinGenerator:")
    test_pincode_generator()

if __name__ == "__main__":
    main()