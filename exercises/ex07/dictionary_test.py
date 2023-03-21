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


from exercises.ex07.dictionary import favorite_color


def test_favorite_color_empty_dict() -> None:
    """This function tests if the favorite_color function will return an empty dictionary if the given dictionary is empty."""
    # one edge case test
    given_dict: dict[str, str] = {}
    assert favorite_color(given_dict) == {}


def test_favorite_color_one_most_frequent() -> None:
    """This function tests if the favorite_color function will return the most frequent color when there is only one."""
    # one use case test
    names_and_colors: dict[str, str] = {"Emily": "red", "Sophia": "green", "Jamie": "green", "Lily": "blue"}
    assert favorite_color(names_and_colors) == "green"


def test_favorite_color_many_most_frequent() -> None:
    """This function tests if the favorite_color function will return the correct most frequent when there is more than one."""
    # one use case test
    names_and_colors: dict[str, str] = {"Emily": "red", "Sophia": "green", "Jamie": "green", "Lily": "red"}
    assert favorite_color(names_and_colors) == "green"