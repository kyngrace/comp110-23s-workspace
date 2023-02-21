"""EX04 - """
__author__ = "730553137"

def all(int_list: list[str], matching_int: int) -> bool:
    """Returns a bool that indicates if all of the ints in the list are the same as the given int."""
    if len(int_list) == 0:
        return False
    if matching_int == int_list:
        return True
    else: 
        return False