"""EX05 - Working with lists and unit tests."""
__author__ = "730553137"

from exercises.ex05.utils import only_evens

def test_only_evens_empty_list() -> None:
    # one edge case test
    given_list: list[int] = []
    assert only_evens(given_list) == []

def test_only_evens_with_mixed_list() -> None:
    # one use case test
    given_list: list[int] = [1, 4, 5, 6, 8, 9]
    assert only_evens(given_list) == [4, 6, 8]

def test_only_evens_with_odd_list() -> None:
    # one use case test
    given_list: list[int] = [3, 5, 7, 11, 15]
    assert only_evens(given_list) == []

from exercises.ex05.utils import concat

def test_concat_empty_lists() -> None:
    # one edge case test
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []

def test_concat_full_lists() -> None:
    # one use case test
    first_list: list[int] = [2, 3, 6]
    second_list: list[int] = [7, 8, 11]
    assert concat(first_list, second_list) == [2, 3, 6, 7, 8, 11]

def test_concat_full_list_and_empty_list() -> None:
    # one use case test
    first_list: list[int] = [2, 3, 6]
    second_list: list[int] = []
    assert concat(first_list, second_list) == [2, 3, 6]