"""EX07 - Working with dictionary utilities."""
__author__ = "730553137"

from exercises.ex07.dictionary import invert, favorite_color, count


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


def test_count_empty_list() -> None:
    """This function tests if the count function will return an empty dictionary when given an empty list."""
    # one edge case test
    given_list: list[str] = []
    assert count(given_list) == {}


def test_count_name_frequency() -> None:
    """This function tests if the count function will return the correct frequency of flower names based on the given list."""
    # one use case test
    flower_names: list[str] = ["daisy", "sunflower", "rose", "rose", "rose"]
    assert count(flower_names) == {"daisy": 1, "sunflower": 1, "rose": 3}


def test_count_num_frequency() -> None:
    """This function tests if the count function will return the correct frequency of numbers based on the given list."""
    # one use case test
    num_list: list[str] = ["1", "1", "2", "4", "6", "6"]
    assert count(num_list) == {"1": 2, "2": 1, "4": 1, "6": 2}