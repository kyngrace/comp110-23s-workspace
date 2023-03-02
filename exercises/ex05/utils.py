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
    combined_list: int = []
    # assigns the combined_list variable to an empty list that will hold the appended ints from the lists
    for ints in first_list:
        # creates a for...in loop that considers the ints in the first list
        combined_list.append(ints)
        # appends the ints from the first list to the combined list
    for ints in second_list:
        # creates a for...in loop that considers the ints in the second list
        combined_list.append(ints)
        # appends the ints from the second list to the combined list 
    return combined_list
    # returns the new created list that contains both the first_list and second_list

def sub(int_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    # declares the function and the names of the parameters
    """Returns a list that is a subset of the input list that stays between the start_idx and the end_idx."""
    if len(int_list) == 0 or start_idx > len(int_list) or end_idx <= 0:
        # checks if the input list is empty or if the start_idx is greater than the length of the input list or if the end_idx is at most 0 (in other words, if they are out of the range)
        return []
        # returns an empty list if the inputted subset is not valid for the conditions/range
    if start_idx < 0:
        # checks if the start_idx is negative
        start_idx: int = 0
        # if it is negative then it gets adjusted to equal zero 
    if end_idx > len(int_list):
        # checks if the end_idx is greater than the length of the inputted list
        end_idx: int = len(int_list)
        # if it is then that means it is too big so it is adjusted to equal the length of the inputted list 
    subset: int = []
    # assigns the subset variable to an empty list that will hold the subsets from the inputted list
    idx: int = start_idx
    # assigns the idx variable to the start_idx so the while loop will start at the beginning of the list 
    for idx in range(start_idx, end_idx, 1):
        # loops through a range of integers that begins at the start_idx and ends at the end_idx
        subset.append(int_list[idx])
        # appends the current int from the int_list to the subset list 
        idx += 1
        # adds one to the idx each time the while loop completes so that it will continue through each part of the list 
    return subset
    # returns the new created subset list 
