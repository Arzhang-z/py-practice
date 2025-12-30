def provide_hint(guess, actual_number):
    #print("your number is too "+ ("low" if guess < actual_number else "high" if guess > actual_number else "correct"))
    if guess < actual_number:
        print("your number is too low")
    elif guess > actual_number:
        print("your number is too high")
