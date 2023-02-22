"""EX04 - 'list' Utility Functions."""
__author__ = "730553137"

def all(int_list: list[int], matching_int: int) -> bool:
    # declares the function and names the parameters
    """Returns a bool that indicates if all of the ints in the list are the same as the given int."""

    int_list_idx: int = 0
    # assigns the int_list_idx variable to track the index of the current int in the int_list
    while int_list_idx < len(int_list):
        # check if the current index is less than the length of int_list
        if matching_int == int_list[int_list_idx]:
            # check is matching_int is equal to the int at the current index in the int_list
            return True
        # return the boolean True
        int_list_idx += 1
        # add one to the index variable so the while loop will loop through the whole int_list
        if len(int_list) == 0:
            # check if the length of the int_list is 0/if the int_list is empty
            return False
        # return the boolean False
        else:
            # check if the ints in the int_list do not match the matching_int
            return False
        # return the boolean False
        
    
    