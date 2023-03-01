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
            # checks if the integer is even
            even_list.append(int)
            # if the integer is even then add it to the outputed even list
    return even_list
    # returns the new created list that contains only even integers

def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    # declares the function and names the parameters
    """Returns a list that combines both input lists without modifying them."""
    combined_list: int = first_list.append(second_list)
    # assigns the combined_list variable that is equal to the first_list and second_list combined
    return combined_list
    # returns the new created list that contains both the first_list and second_list

def sub(int_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Returns a list that is a subset of the input list that stays between the start_idx and the end_idx."""
    