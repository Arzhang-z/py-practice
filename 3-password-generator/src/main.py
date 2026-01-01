import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download("words")

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length
    
    def generate(self) -> str:
        return "".join([random.choice(string.digits) for _ in range(self.length)])


class RandomPaswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return "".join([random.choice(self.characters) for _ in range(self.length)])
    

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        number_of_words: int = 4,
        seperator: str = "_",
        capitalization: bool = False,
        vocabulary: list = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.number_of_words = number_of_words
        self.capitalize = capitalization
        self.seperator = seperator


    def generate(self) -> str:
        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalize:
            # 50% of words to be capitalize
            password_words = [word.upper() if random.choice([True,False]) else word.lower() for word in password_words]
        
        return self.seperator.join(password_words)
    

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
    password_generator = MemorablePasswordGenerator(7,"_",True,None)
    print(password_generator.generate())
