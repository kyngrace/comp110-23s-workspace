"""EX04 - Working with lists."""
__author__ = "730553137"


def all(int_list: list[int], matching_int: int) -> bool:
    # declares the function and names the parameters
    """Returns a bool that indicates if all of the ints in the list are the same as the given int."""
    int_list_idx: int = 0
    # assigns the int_list_idx variable to track the index of the current int in the int_list
    if len(int_list) == 0:
        # check if the length of the int_list is 0/if the int_list is empty
        return False
    # return the boolean False
    while int_list_idx < len(int_list):
        # check if the current index is less than the length of int_list
        if matching_int != int_list[int_list_idx]:
            # check if matching_int is not equal to the int at the current index in the int_list
            return False
            # return the boolean False
        int_list_idx += 1
        # add one to the index variable so the while loop will loop through the whole int_list
    return True
    # return the boolean True


def max(input: list[int]) -> int:
    # declares the function and names the parameter
    """Returns the maximum integer from a given list or returns a ValueError for an empty list."""
    if len(input) == 0:
    # check if the input list is empty
        raise ValueError("max() arg is an empty List")
        # raise a ValueError with a specific error message
    max_int: int = input[0]
    # initialize the maximum integer to the first integer in the list
    counter: int = 0
    # create a counter variable and initialize it to 0
    while counter < len(input):
    # check if counter is less than the length of the input list
        if input[counter] > max_int:
        # check if the current integer being checked is larger
            max_int = input[counter]
            # update the maximum integer
        counter += 1
        # counter variable moves on to the next integer in the list
    return max_int
   # return the value of the final maximum integer


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    # declares the function and names the parameters
    """Returns a bool that indicates if every element at every index is equal in both lists."""   
    if len(int_list1) != len(int_list2):
    # check if the lengths of int_list1 and int_list2 are equal
        return False
        # return False if the lengths of the two lists are not equal
    idx: int = 0
    # initialize an indexing variable
    while idx < len(int_list1):
    # compare the integers in both of the lists at a certain index
        if int_list1[idx] != int_list2[idx]:
        # check if the integers at the index are equal
            return False
            # if the integers are not equal, return False
        idx += 1
        # add 1 to the indexing variable so the while loop while continue through the list
    return True
   # if the while loop gets to this point then that means the lists have not returned False and they are equal so, return True