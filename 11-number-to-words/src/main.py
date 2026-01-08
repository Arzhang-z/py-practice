from constants import UNDER_20, TENS, ABOVE_100


def num_to_word(num: int) -> str:
    """
    Convert number to its word representation
    note: This function only works for numbers less than 10^15 and equal or greater than 0
    
    :param num: The number to convert.
    :return: The word representation of the number.

    >>> num_to_word(0)
    'Zero'
    """
    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        return TENS[num // 10] + (" "+UNDER_20[num % 10] if num%10 != 0 else "")
    
    pivot = max([key for key in ABOVE_100.keys() if key <= num])
    p1 = num_to_word(num // pivot)
    p2 = ABOVE_100[pivot]
    
    return f'{p1} {p2}{" " + num_to_word(num % pivot) if num % pivot != 0 else ""}'


def check_valid():
    assert num_to_word(0) == "Zero"
    assert num_to_word(23) == "Twenty Three"
    assert num_to_word(148) == "One Hundred Forty Eight"
    assert num_to_word(26987) == "Twenty Six Thousand Nine Hundred Eighty Seven"
    assert num_to_word(100000000000) == "One Hundred Billion"

if __name__ == "__main__":
    check_valid()

    while True:
        try:
            num = int(input("\nEnter Your Number: "))
        except TypeError as e: 
            print(f"Please Entr an integer! {e}")
            continue

        print(num_to_word(num))

        replay = input("Do you wanna play again?[y/n] ")
        if "y" in replay.lower():
            continue
        else:
            print("Program Shutting Down...")
            break
