"""EX03 - Wordle - Make your best guess!"""
__author__ = "730553137"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, character: str) -> bool:
    """Returns a character that is being searched for"""
    word_idx: int = 0

    assert len(character) == 1
    while word_idx < len(word):
        if word[word_idx] == character:
            return True
        
        word_idx += 1

    return False    

def emojified(guess: str, secret: str) -> str: 
    """Returns a string of emoji based on a characters appearance"""

    secret_idx: int = 0
    emoji: str = ""
    assert len(guess) == len(secret)
    while secret_idx < len(secret):
        if guess[secret_idx] == secret[secret_idx]:
            emoji += GREEN_BOX
        else: 
            does_word_exist: bool = contains_char(secret, guess[secret_idx])
            
            if does_word_exist:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        secret_idx = secret_idx + 1
    return emoji

def input_guess(expected_length: int) -> str:
    """Prompts user for a guess until they provide one of the correct length"""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess 

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 0
    you_won: bool = False

    while turns < 6 and not(you_won):
        print(f"=== Turn {turns +1}/6 ===")
        guess = input_guess(secret)
        #3
        if guess == secret:
            you_won: bool = True
        turns += 1
    if you_won:
        print(f"You won in {turns}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")

    if __name__ == "__main__":
        main()
