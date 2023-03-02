"""EX05 - Working with lists and unit tests."""
__author__ = "730553137"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens_empty_list() -> None:
    """This function tests the only_evens function with an empty list and makes sure it returns an empty list when the given list is empty."""
    # one edge case test
    given_list: list[int] = []
    assert only_evens(given_list) == []

def test_only_evens_with_mixed_list() -> None:
    """This function tests the only_evens function with a mixed list and makes sure it only returns the even ints from the given list."""
    # one use case test
    given_list: list[int] = [1, 4, 5, 6, 8, 9]
    assert only_evens(given_list) == [4, 6, 8]

def test_only_evens_with_odd_list() -> None:
    """This function tests the only_evens function with an odd list and makes sure that it returns an empty list since there are no even numbers."""
    # one use case test
    given_list: list[int] = [3, 5, 7, 11, 15]
    assert only_evens(given_list) == []

def test_concat_empty_lists() -> None:
    """This function tests the concat function with an empty list and makes sure it returns an empty list because that is what the two empty lists combine to."""
    # one edge case test
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []

def test_concat_full_lists() -> None:
    """This function tests the concat function with a full list and makes sure it returns the first_list and second_list combined."""
    # one use case test
    first_list: list[int] = [2, 3, 6]
    second_list: list[int] = [7, 8, 11]
    assert concat(first_list, second_list) == [2, 3, 6, 7, 8, 11]

def test_concat_full_list_and_empty_list() -> None:
    """This function tests the concat function with a full list and an empty list and makes sure it returns no more or less than the full given list."""
    # one use case test
    first_list: list[int] = [2, 3, 6]
    second_list: list[int] = []
    assert concat(first_list, second_list) == [2, 3, 6]

def test_sub_empty_list() -> None:
    """This function tests the sub function with an empty list to make sure that with a certain start_idx and end_idx the correct list output is returned."""
    # one edge case test
    assert sub([], 0, 0) == []
    assert sub([], -1, 1) == []
    assert sub([], 0, 1) == []
    assert sub([], -1, 0) == []
    assert sub([], 1, 0) == []
    assert sub([], 0, -1) == []

def test_sub_valid_list() -> None:
    """This function tests the sub function with a valid input list to make sure that the returned list follows the valid start_idx and end_idx."""
    # one use case test
    int_list: list[int] = [1, 2, 4, 7, 9]
    start_idx: int = 1
    end_idx: int = 4
    assert sub(int_list, start_idx, end_idx) == [2, 4, 7]

def test_sub_invalid_start_idx() -> None:
    """This function tests the sub function with an invalid start_idx to make sure that the correct list is returned."""
    # one use case test
    int_list: list[int] = []
    start_idx: int = 4
    end_idx: int = 6
    assert sub(int_list, start_idx, end_idx) == []