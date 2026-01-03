import random
from typing import Tuple


def monty_hall_game(switch_doors: bool = False) -> bool:
    doors = ["car"] + ["goat"] * 2
    random.shuffle(doors)

    initial_choice = random.choice(range(3))
    
    if switch_doors:
        doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != "car"]
        door_revealed = random.choice(doors_revealed)
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    
    return doors[final_choice] == "car"

def simulate_game(num_games: int = 1000) -> Tuple[float, float]:
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(num_games)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])
    return num_wins_without_switching / num_games, num_wins_with_switching / num_games


if __name__ == "__main__":
    num_games = int(input("number of games to be played? "))
    win_percent_without_switching, win_percent_with_switching = simulate_game(num_games)
    print(f" Win percent with switching : {100*win_percent_with_switching: .2f} %")
    print(f" Win percent without switching : {100*win_percent_without_switching: .2f} %")