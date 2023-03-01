"""EX05 - Working with lists and unit tests."""
__author__ = "730553137"

def only_evens(given_list: list[int]) -> list[int]:
    # declares the function and names the parameter
    """Returns a list from the input list with only the even numbers."""
    even_list: list[int] = []
    # assigns the even_list variable and creates an empty list to keep even integers
    for int in given_list:
        # creates a for...in loop to iterate through each integer in the given list
        if int % 2 == 0:
            # check if the integer is even
            even_list.append(int)
            # if the integer is even then add it to the outputed even list
    return even_list
    # return the new created list that contains only even integers
