"""File to define Fish class."""
__author__ = "730553137"
class Fish:

    # attributes
    age: int
    
    def __init__(self, age_input: int = 0):
        self.age: int = age_input
        return None
    
    def one_day(self):
        self.age += 1
        return None