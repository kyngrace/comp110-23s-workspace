"""EX07 - Working with dictionary utilities."""
__author__ = "730553137"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    # declares the function and names the parameter 
    """Returns a dictionary that swaps the values and keys between the given and output list."""
    inverted_dict: dict[str, str] = {}
    # initializes the inverted_dict variable to an empty dictionary to hold the inverted keys and values
    for key in given_dict:
        # creates a for loop that loops through each key in the given dictionary 
        value: str = given_dict[key]
        # initializes the value variable in order to make it equal to the current key being looped through in the dictionary 
        if value in inverted_dict:
            # checks if the value already exists as a key once inverted 
            raise KeyError(f"Error! {value} already exists in the inverted dictionary as a key.")
        # raises a KeyError
        else:
            # if it gets to this point in the loop then the key/value pair is added to the inverted dictionary
            inverted_dict[value] = key
    return inverted_dict
    # returns the inverted dictionary


def favorite_color(names_and_colors: dict[str, str]) -> str:
    # declares the function and names the parameter 
    """Returns the color that is most frequent throughout the dictionary and if there is a tie for frequency returns the one that appeared first."""
    if not names_and_colors:
        # checks if the given dictionary is empty
        return {}
        # returns an empty dictionary 
    color_tracker: dict[str, int] = {}
    # creates an empty dictionary to keep track of the frequency of each color
    for name in names_and_colors:
        # creates a for loop that will loop over each value of the given dictionary
        color: str = names_and_colors[name]
        # initializes the color variable that will find the color value that goes with the given name
        if color in color_tracker:
            # checks if the color is already being counted in the tracker 
            color_tracker[color] += 1
            # if the color is already being counted then it adds one to the total count
        else:
            # checks if the color has not already been counted in the tracker
            color_tracker[color] = 1
            # adds 1 to the tracker for the color that has not already appeared in the dictionary 
    most_frequent: str = ""
    # intializes an empty list that will keep track of the most frequent color
    max_amount: int = 0
    # creates a variable to track the max count for the colors 
    for amount in color_tracker[color]:
        # creates a for loop that checks the amount of times a certain color appears in the given dictionary 
        if amount > max_amount:
            # checks if the amount of times the color appears is greater than the max amount another color appears 
            most_frequent = color
            # updates the most frequently occuring color if it appears more than the max amount
            max_amount = amount
            # updates the max amount so that the loop will know what amount to compare to other colors as it repeats
        elif amount == max_amount and color < most_frequent:
            # checks if there is the same amount of frequency (the max amount) between more than one color 
            most_frequent = color
                # makes the most frequent equal to the color that appeared first in the dictionary 
    return most_frequent
    # returns the most frequent color


def count(value_list: list[str]) -> dict[str, int]:
    # declares the function and names the parameter
    """Returns a dictionary that contains the counts of each item in the given list."""
    result: dict[str, int] = {}
    # intializes the result variable and creates an empty dictionary to hold the result
    for value in value_list:
        # creates a for loop that will loop through each value in the given value list
        if value in result:
            # checks if the current value being looped through is already a key in the result dictionary 
            result[value] += 1
            # if it is then add one to the value associated with the key
        else:
            # checks if the current value being looped through is not already a key in the result dictionary 
            result[value] = 1
            # if it is not then add a new key-value pair to the result dictionary that will have a value of 1
    return result
    # returns the resulting dictionary 