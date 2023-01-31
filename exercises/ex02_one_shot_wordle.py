"""EX02 - Wordle - Guess what the word is!"""
__author__ = "730553137"

secret_word: str = "python"

secret_word_idx: int = 0

input("What is your 6-letter guess? ")
while secret_word_idx != len(secret_word):
    input("That was not 6 letters! Try again: ")
    secret_word_idx = secret_word_idx +1
while secret_word_idx == len(secret_word):
    if secret_word == secret_word:
        print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
