def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Returns a bool that indicates if every element at every index is equal in both lists."""
    idx = 0
    while idx < len(int_list1):
        if len(int_list1) == len(int_list2):
            return True
        else: 
            return False
    idx += 1
    
def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Returns a bool that indicates if every element at every index is equal in both lists."""
    if len(int_list1) != len(int_list2):
        return False
    idx = 0
    while idx < len(int_list1):
        if int_list1[idx] != int_list2[idx]:
            return False
        idx += 1
    return True