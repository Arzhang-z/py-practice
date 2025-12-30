from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_genrator import provide_hint
from src.game_logic.scorer import Scoree
from src.game_logic.play_again import play_again


def main():
    score = Scoree(100)
    actual_number = generate_random_number(1,100)

    while True:
        user_input = get_valid_input("Enter a number between",1,100)
        if user_input == actual_number:
            print("you guessed the number correctly!")
            print(f"your score is {score.total_score()}.")
            if play_again():
                score = Scoree(100)
                actual_number = generate_random_number(1,100)
                continue
            else:
                print("Thank you for playing! Goodbye!")
            break

        else:
            provide_hint(user_input,actual_number)
            score.decrement(10)

        if score.total_score() <= 0:
            print("Game Over! You ran out of guesses!")
            print(f"The correct number was {actual_number}.")
            if play_again():
                score = Scoree(100)
                actual_number = generate_random_number(1,100)
                continue

if __name__ == "__main__":
    main()