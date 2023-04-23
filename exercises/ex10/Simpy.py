"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730553137"


class Simpy:
    """Working with Simpy."""
    
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, input_values: list[float]):
        """Set the values attribute equal to the input_values argument."""
        self.values = input_values
        # sets the self.values attribute equal to the input_values argument

    def __str__(self) -> str:
        """Convert what we get as output from the above method into a string and then returns that string."""
        return f"Simpy({str(self.values)})"
    # creates a string to return
    
    def fill(self, val: float, val_count: int) -> None:
        """Fill Simpys values with a specific number of repeating values."""
        self.values = [val] * val_count
        # creates a new list that is repeated val_count times and initializes it to the self.values attribute 

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of values."""
        assert step != 0.0
        # makes sure there is no infinite loop since step cannot be 0.0
        if start < stop:
            # checks if the range is positive
            while start < stop:
                self.values.append(start)
                start += step
        else:
            # checks if the range is negative
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        return sum(self.values)
    # uses the built-in sum function

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use the addition opperator in conjunction with Simpy objects and floats."""
        if type(rhs) == float:
            # checks if the type of the rhs argument is a float
            return Simpy([val + rhs for val in self.values])
        elif type(rhs) == Simpy:
            # checks if the type of the rhs argument is Simpy
            assert len(self.values) == len(rhs.values)
            return Simpy([self.values[idx] + rhs.values[idx] for idx in range(len(self.values))])
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add the ability to use the power operator in conjunction with Simpy objects and floats."""
        if type(rhs) == float:
            # checks if the type of the rhs argument is float
            return Simpy([val ** rhs for val in self.values])
        elif type(rhs) == Simpy:
            # checks if the type of rhs argument is Simpy
            assert len(self.values) == len(rhs.values)
            return Simpy([self.values[idx] ** rhs.values[idx] for idx in range(len(self.values))])
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add the ability to produce a mask based on the equality of each item in the values attribute with some other Simpy object or a float value."""
        if type(rhs) == float:
            # checks if the type of the rhs argument is float
            return [val == rhs for val in self.values]
        elif type(rhs) == Simpy:
            # checks if the type of the rhs argument is Simpy
            assert len(self.values) == len(rhs.values)
            return [self.values[idx] == rhs.values[idx] for idx in range(len(self.values))]
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add the ability to produce a mask based on the greater than relationship between each item in the values attribute with some other Simpy object or a float value."""
        if type(rhs) == float:
            # checks if the type of the rhs argument is float
            return [val > rhs for val in self.values]
        elif type(rhs) == Simpy:
            # checks if the type of the rhs argument is Simpy
            assert len(self.values) == len(rhs.values)
            return [self.values[idx] > rhs.values[idx] for idx in range(len(self.values))]
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Take either an int in the first usage or a list[bool] in the second usage and return either a single float value or a new Simpy object."""
        if type(rhs) == int:
            # checks if the type of the rhs argument is int
            return self.values[rhs]
        elif type(rhs) == list and len(rhs) == len(self.values):
            # checks if the type of the rhs argument is a list and if its length matches the length of the self.values atrribute
            new_values: list = []
            for val in range(len(self.values)):
                if rhs[val]:
                    new_values.append(self.values[val])
            return Simpy(new_values)
