"""EX07 - Working with dictionary utilities."""
__author__ = "730553137"


def invert(given_dict: dict[str, str]) -> dict[str, list[str]]:
    # declares the function and names the parameter 
    """Returns a dictionary that swaps the values and keys between the given and output list."""
    inverted_dict: dict[str, list[str]] = {}
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
            inverted_dict[value] = [key]
    return inverted_dict
        # returns the inverted dictionary 