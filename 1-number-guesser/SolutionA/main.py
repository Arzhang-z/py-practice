import random

def validate_input(user_guess):
    if not user_guess.isdigit():
        print("Invalid Input. Please try again later.")
        return False

    user_guess = int(user_guess)
    if (user_guess > 100) or (user_guess <= 0):
        print("Your guess is out of range, Please try again later, Your guess must be between 1 and 100.")
        return False
    
    return True

def play_agian():
    while True:
        user_input =input("Do you wanna play again?")
        if type(user_input) != str:
            print("please enter txt message only")
            continue
        
        user_input = str(user_input)
        if "n" in user_input.lower():
            print("Okay thanks for playing bye!")
            return False
        elif "y" in user_input.lower():
            return True

def main():
    rand_num = random.randint(1,100)

    score = 100

    while True:
        user_guess = input("Guess a number between 1 and 100: ")
        
        if user_guess == "q":
            print("thank you for playing.Goodbye!")
            break
        
        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)
        if rand_num < user_guess:
            print("Your guess is to high.")
        elif rand_num > user_guess:
            print("your guess is too low")
        else:
            print("Congartulations, your guess was right!")
            print(f"your score is :{score}")
            if play_agian() != False:
                main()
            break
        
        score -= 10
        if score <= 0:
            print("you ran out of guesses  thanks for playing")
            if play_agian() != False:
                main()
            break



if __name__ == '__main__':
    main()
