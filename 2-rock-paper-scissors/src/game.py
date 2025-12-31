"""
Author: Arzhang-z
Date Created: 12/31/2025
Description: Rock Paper Scissors game.
"""


import random


class RockPaperScissors:
    """Main class for Rock Paper Scissors game
    """
    def __init__(self):
        self.choices = ["rock","paper","scissors"]
        self.win_count = 0
        self.tie_count = 0
        self.total = 0

    def get_player_choice(self):
        user_choice = input(f"Enter your choie ({self.choices}) ")
        if user_choice.lower() in self.choices :
            # print(f"You chose ({user_choice.lower()})")
            return user_choice.lower()
        
        print(f"Invalid Choice! You must select from ({self.choices}) ")
        return self.get_player_choice()

    def get_computer_choice(self):
        """Get Computer Choice randomly from Choices: rock, paper, scissors."""
        return random.choice(self.choices)
    
    def decide_winner(self,user_choice: str,computer_choice: str):
        """Decide the winner of the game based on user and computer choices
        
        :param user_choice: choice of user
        :param computer_choice: choice of computer
        :return: result of the game
        """
        print(f"YOU CHOSE: ({user_choice})")
        print(f"COMPUTER CHOSE: ({computer_choice})")
        
        if user_choice == computer_choice:
            self.tie_count += 1
            return "Its a Tie!"

        win_combinations = [("rock" , "scissors"), ("paper","rock"), ("scissors","paper")]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                self.win_count += 1
                return f"Congratulations! You won! you won {self.win_count} times !"
            
        return f"Oh No! The computer Won! Computer won {self.total - (self.win_count + self.tie_count)} times !"    

    def play(self):
        """Play the game
        - Get user choice
        - Get computer choice
        - Decide the winner
        - Print the result
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        self.total += 1
        print(self.decide_winner(user_choice,computer_choice))

    def stats(self):
        return f"your were {100 * self.win_count/(self.total)} % accurate in total of {self.total} times"


if __name__ == "__main__":
    game = RockPaperScissors()
    while True:
        game.play()
        
        continue_game = input("Do you wanna play again? (Enter any key to begin, enter q to exit)")
        if continue_game.lower() == "q":
            print(game.stats())
            break
