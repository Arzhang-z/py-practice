import random
import string
from abc import ABC, abstractmethod

import nltk

# Do it Once then comment it
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
        self.number_of_words = int(number_of_words)
        self.capitalize = capitalization
        self.seperator = seperator


    def generate(self) -> str:
        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalize:
            # 50% of words to be capitalize
            password_words = [word.upper() if random.choice([True,False]) else word.lower() for word in password_words]
        
        return self.seperator.join(password_words)
    
if __name__ == "__main__":
    args = ["number of words: int", "seperator: str", "capitalization: bool"]    
    user_inputs = [input(f"please enter input number {i+1}, {args[i]} ") for i in range(3)]
    inp_1 = int(user_inputs[0])
    inp_2 = user_inputs[1]
    inp_3 = user_inputs[2].lower == "true"
    password_generator = MemorablePasswordGenerator(inp_1,inp_2,inp_3,vocabulary=None)
    print(password_generator.generate())