"""EX02 - Wordle - Guess what the word is!"""
__author__ = "730553137"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
# reassigning the guess variable
while len(guess) != len(secret_word):
    # check if the length of a guess is not equal to the length of the secret word
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word_idx: int = 0
emoji_result: str = ""

while secret_word_idx < len(secret_word):
    # check the position of letters in the secret word 
    if guess[secret_word_idx] == secret_word[secret_word_idx]:
        # check if the position of the letters in a guess matches the position of the letters in the secret word
        emoji_result += GREEN_BOX
    else: 
        does_it_exist: bool = False
        track_keeper: int = 0
        while not (does_it_exist) and (track_keeper < len(secret_word)):
            # check if the boolean variable is not true and the indexing variable is less than the length of the secret word 
            if secret_word[track_keeper] == guess[secret_word_idx]:
                # check if the alternate position of the secret word matches the current position of a guess
                does_it_exist = True
            else: 
                track_keeper += 1
        if does_it_exist:
            # check if boolean variable is True and then add the correct emoji box
            emoji_result += YELLOW_BOX
        else:
            # check if the boolean variable is False and then add the correct emoji box
            emoji_result += WHITE_BOX
    secret_word_idx = secret_word_idx + 1
print(emoji_result)

if guess != secret_word:
    # check if guess is not the secret word
    print("Not quite. Play again soon!")
if guess == secret_word:
    # check if guess is the secret word
    print("Woo! You got it!")  