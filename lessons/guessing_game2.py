"""Asks user to guess a number, if number is in string, they win"""

SECRET_STRING: str = "2468"
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing: 
    #check to see if the guess is in the secret string
    string_idx: int = 0
    found: bool = False
    while string_idx < len(SECRET_STRING):
        if int(SECRET_STRING[string_idx]) == guess:
            #if it is, print "You got it!" and playing = False
            print("You got it!")
            playing = False
            found = True
        string_idx = string_idx + 1
    if not found: 
        #if it is not in the string, then ask for another guess
        print("Guess again!")
        guess = int(input("New guess here: "))
        
   