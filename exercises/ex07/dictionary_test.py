"""EX07 - Working with dictionary utilities."""
__author__ = "730553137"

from exercises.ex07.dictionary import invert


def test_invert_empty_dict() -> None:
    """This function tests if the invert function will return an empty dictionary if the given dictionary is empty."""
    # one edge case test
    given_dict: dict[str, str] = {}
    assert invert(given_dict) == {}


def test_invert_expected_output() -> None:
    """This function tests if the invert function will return the expected output based on a given dictionary."""
    # one use case test
    given_dict: dict[str, str] = {"b": "2", "d": "4", "f": "6"}
    expected_output: dict[str, str] = {"2": ["b"], "4": ["d"], "6": ["f"]}
    assert invert(given_dict) == expected_output


def test_invert_easy_input() -> None:
    """This function tests if the invert function will return an output correctly based on a simple input."""
    # one use case test 
    assert invert({"t": "2", "f": "5", "c": "6"}) == {"2": ["t"], "5": ["f"], "6": ["c"]}