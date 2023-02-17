"""EX03 - Wordle - Make your best guess!"""
__author__ = "730553137"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# above 3 lines assign the constants


def contains_char(word: str, character: str) -> bool:
    # declares the function and names the parameters
    """Returns a character that is being searched for."""
    word_idx: int = 0
    # assigns the word_idx variable

    assert len(character) == 1
    # asserts the assumption that an error will be raised if this is not found to be true
    while word_idx < len(word):
        # check if word_idx is less than the length of the word
        if word[word_idx] == character:
            # check if the character of the word is the chracter that is being searched for 
            return True
        # returns True if the character of the word is the character that is being searched for
        
        word_idx += 1
        # adds one to the word_idx so that a new character of the word is being looked at each time the while loop is gone through

    return False
# returns False if the word_idx is not less than the length of the word    


def emojified(guess: str, secret: str) -> str:
    # declares the function and the names of the parameters 
    """Returns a string of emoji based on a characters appearance."""
    secret_idx: int = 0
    # assigns the secret_idx variable
    emoji: str = ""
    # assigns the emoji variable 
    assert len(guess) == len(secret)
    # asserts that strings of equal length are being provided
    while secret_idx < len(secret):
        # checks the position of the letters in the secret word
        if guess[secret_idx] == secret[secret_idx]:
            # checks if the letter in a certain position of the guess is the same as the letter in a certain position of the secret
            emoji += GREEN_BOX
            # if the letters are the same and in the same position then a green box emoji is printed
        else: 
            does_letter_exist: bool = contains_char(secret, guess[secret_idx])
            # assigns the does_letter_exist variable and calls the contains_char function
            
            if does_letter_exist:
                # checks if the letter exists but not in the correct position
                emoji += YELLOW_BOX
                # if the letter does exist in the word but in the wrong position then a yellow box is printed
            else:
                # checks if the letter does not exist in the word at all 
                emoji += WHITE_BOX
                # if the letter does not exist at all then a white box is printed
        secret_idx = secret_idx + 1
        # adds one to the secret_idx variable each time the while loop is gone through so a new character will be searched through 
    return emoji
# returns the emoji string


def input_guess(expected_length: int) -> str:
    # declares the function and the name of the parameter 
    """Prompts user for a guess until they provide one of the correct length."""
    guess = input(f"Enter a {expected_length} character word: ")
    # assigns the guess variable 
    while len(guess) != expected_length:
        # checks if the length of the guess is the length of the secret word
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
        # reassigns the guess variable 
    return guess
# returns the guess  


def main() -> None:
    # declares the function
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    # assigns the secret variale 
    turns: int = 0
    # assigns the turns variable 
    you_won: bool = False
    # assigns the you_won variable 

    while turns < 6 and not (you_won):
        # checks if the amount of turns are less than 6 and you haven't guessed the correct word 
        print(f"=== Turn {turns +1}/6 ===")
        # prints the current turn
        guess = input_guess(len(secret))
        # asks the user for a guess and calls the input_guess function 
        print(emojified(guess, secret))
        # prints the resulting string of emojis based on the guess and calls the emojified function
        if guess == secret:
            # checks if the guess is equal to the secret 
            you_won = True
            # if the guess is equal to the secret then the you_won boolean variable becomes True
        turns += 1
        # adds 1 to the amount of turns each time the while loop is gone through so you get a new turn until you have had 6
    if you_won:
        # checks if you won the game by guessing the secret word 
        print(f"You won in {turns}/6 turns!")
        # if you did win the game then it prints out the statement
    else: 
        # checks if you did not win the game because you didn't guess the right word 
        print("X/6 - Sorry, try again tomorrow!")
        # if you did not win the game then it prints this statement 

    if __name__ == "__main__":
        main()
        # makes it possible for the python program to be ran as a module and for other modules to import the functions and reuse them