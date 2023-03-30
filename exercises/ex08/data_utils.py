"""EX08 - Working with Jupyter Notebooks and data."""
__author__ = "730553137"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    # step through table
    for row in table:
        # save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, list[str]] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    # Declares the head function and its parameters 
    """Returns a new column-based table that has only the first N rows of data for each column."""
    new_table: dict[str, list[str]] = {}
    # Creates a variable that is initialized to an empty dictionary 
    for column in column_table:
        # Loops through each of the columns in the first row
        first_N: list[str] = []
        # Creates empty list to hold the first N values in each column
        for idx in range(N):
            # Loops through first N items of the tables column
            if idx < len(column_table[column]):
                # Checks if the column has more than idx values, append the value to the first_N list 
                first_N.append(column_table[column][idx])
                # Removes and appends the first elem of the current column's list to the first_N list
                new_table[column] = first_N
                # Adds the resulting list to the dictionary that will be output 
    return new_table
# Returns the dictionary/new table


def select(given_column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    # Declares the select function and its parameters
    """Produces a new column-based table with only a specific subset of the original columns."""
    new_table: dict[str, list[str]] = {}
    # Creates a new variable that is initialized to an empty dictionary 
    for column in column_names:
        # Loops through each column that is provided in column_names
        if column in given_column_table:
            # Checks if the name of the column already exists in the new_column_table
            new_table[column] = given_column_table[column]
            # Assigns the column key of the new dictionary to the list of values that are being stored in the given dictionary at the same column being looped through 
    return new_table
# Returns the dictionary/new table


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    # Declares the concat function and its parameters
    """Produces a new column_based table with two column based tables combined."""
    new_table: dict[str, list[str]] = {}
    # Creates a new variable that is intialized to an empty dictionary 
    for column in table_one:
        # Loops through the columns in table_one
        new_table[column] = table_one[column]
        # After the columns are looped through, this adds/copies them to the new_table
    for column in table_two:
        # Loops through the columns in table_two
        if column in new_table:
            # Checks if the column key being looped through already exists in the new_table
            for val in table_two[column]:
                new_table[column].append(val)
            # Adds the new values to the new_table if they already exist
        else:
            # Checks if the column does not already exist in the new_table
            new_table[column] = table_two[column]
            # Creates a new column and adds/copies the values to the new_table
    return new_table
# Returns the dictionary/new table


def count(val_list: list[str]) -> dict[str, int]:
    # Declares the count function and its parameter
    """Returns the number of times a certain value appeared in the given list."""
    times: dict[str, int] = {}
    # Creates the times variable and initializes it to an empty dictionary 
    for val in val_list:
        # Loops through each value in the given list
        if val in times:
            # Checks in the value is already in the output dictionary 
            times[val] += 1
            # If it is then it increases the amount of times it appears by one
        else:
            # Checks if the value is not already in the output dictionary
            times[val] = 1
            # If it is not then it adds it to the dictionary 
    return times
# Returns the amount of times a certain values appeared in the given list