import random


class TicTacToe:
    def __init__(self):
        self.board: list[str] = [" "] * 10 #list(map(str, range(10))) # 0th index is not used
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        return random.choice(["X","O"])

    def show_board(self):
        print("\n")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-----")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-----")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print("\n")

    def swap_player_turn(self) -> str:
        self.player_turn = "X" if self.player_turn != "X" else "O"
        return self.player_turn
    
    def is_board_filled(self) -> bool:
        return " " not in self.board[1:]

    def fix_spot(self, cell: int, player: str):
        self.board[cell] = player

    def has_player_won(self, player: str) -> bool:
        win_combination = [
            [1,2,3], [4,5,6], [7,8,9],  # rows
            [1,4,7], [2,5,8], [3,6,9],  # columns
            [1,5,9], [3,5,7]            # diagonals
        ]

        for combination in win_combination:
            if all([self.board[cell] == player for cell in combination]):
                return True
        return False
    
    def validate_input(self, cell: int) -> bool:
        if (cell < 1) or (cell > 9):
            print("Input out of range Enter Valid cell numebr from 1 to 9: ")
            return False
        
        if self.board[cell] != " ":
            print("This cell have laready been chosen, try another cell ")
            return False
        
        return True

    def reset(self):
        self.board = [" "] * 10
        self.player_turn = self.get_random_first_player()

    def play_again(self):
        while True:
            user_choice = input("Do you wanna play again?[y/n]")
            
            if "y" in user_choice.lower():
                self.reset()
                self.start()
                break

            elif "n" in user_choice.lower():
                print("Thanks for playing!")
                break

    def start(self):
        while True:    
            self.show_board()
            print(f"Player {self.player_turn} turn")
            
            try:
                cell = int(input("Enter cell numebr from 1 to 9: "))
            
            except ValueError:
                continue
            
            if not self.validate_input(cell):
                continue

            self.fix_spot(cell,self.player_turn)
            if self.has_player_won(self.player_turn):
                self.show_board()
                print(f"player {self.player_turn} won!")
                self.play_again()
                break

            self.swap_player_turn()
        
            if self.is_board_filled():
                print("Draw!")
                self.play_again()
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.start()
