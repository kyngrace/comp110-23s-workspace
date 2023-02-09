"""In class function practice"""

my_words: str = "Hello!"
letter_idx: int = 0
mimic_letter: str = "0"
response: str = mimic_letter(my_words)


def mimic_letter(my_words: str, letter_idx: int) -> str: 
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        print("Index too high")
    #If we made it here, that means the letter_idx is valid
    return my_words[letter_idx]
print(response)
