"""File to define Fish class."""
__author__ = "730553137"


class Fish:
    """Declares the class Fish."""

    # attributes
    age: int
    
    def __init__(self, age_input: int = 0):
        """Declares the __init__ function to keep begin tracking age of fish."""
        self.age: int = age_input
        return None
    
    def one_day(self):
        """Declares the one_day function to increase the age by 1."""
        self.age += 1
        # Increase age by 1
        return None