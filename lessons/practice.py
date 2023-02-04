"""Practicing while loops!"""
__author__ = "730553137"

secret: int = 10
guess: int = (int(input("Guess the number! ")))
playing: bool = True

while playing:
    if guess == secret: 
        print("Correct! You got the right answer! :)")
        playing = False