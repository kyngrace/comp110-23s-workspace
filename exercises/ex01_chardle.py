"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730553137"

one_word: str = input("Enter a 5-character word: ")
if len(one_word) != 5:
    print("Error: Word must contain 5 characters ")
one_letter: str = input("Enter a single character: ")  
if len(one_letter) != 1:
    print("Error: Character must be a single character.")
counter = 0
print("Searching for " + one_letter + " in " + one_word)
if one_letter == one_word[0]:
    print(one_letter + " found at index 0")
    counter += 1
if one_letter == one_word[1]:
    print(one_letter + " found at index 1")
    counter += 1
if one_letter == one_word[2]:
    print(one_letter + " found at index 2")
    counter += 1
if one_letter == one_word[3]:
    print(one_letter + " found at index 3")
    counter += 1
if one_letter == one_word[4]:
    print(one_letter + " found at index 4")
    counter += 1

print(counter)
if (counter == 1):
    print(counter, "instance of " + one_letter + " found in " + one_word)
elif (counter > 1):
    print(counter, "instances of " + one_letter + " found in " + one_word)
else: 
    print("No instances of " + one_letter + " found in " + one_word)