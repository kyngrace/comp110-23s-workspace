"""EX04 - 'list' Utility Functions."""
__author__ = "730553137"

def all(int_list: list[str], matching_int: int) -> bool:
    """Returns a bool that indicates if all of the ints in the list are the same as the given int."""

    int_list_idx: int = 0
    while int_list_idx < len(int_list):
        matching_int = int_list[0]
        int_list_idx += 1  
        if matching_int == int_list:
            return True
        if len(int_list) == 0:
            return False
        else: 
            return False
        
    
    