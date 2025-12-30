def play_again():
	user_input = str(input("Do You Wanna Play Again? [Yes/No] "))
	if "y" in user_input.lower():
		return True
	elif "n" in user_input.upper():
		return False
