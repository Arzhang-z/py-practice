def get_valid_input(prompt, start, end):
    while True:
        try:
            user_input = int(input(prompt + str(start) + "and "+ str(end) + ":  " ))
            if start <= user_input <= end:
                return user_input
            else:
                print(f"invalid input. please enter a number between {start} and {end}. ")
                continue
        except ValueError:
            print("Invalid input. Please enter a number. ")
            continue

if __name__ == "__main__":
    print(get_valid_input("Enter a number between ",1,10))



