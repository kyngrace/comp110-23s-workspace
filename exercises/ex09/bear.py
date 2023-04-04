"""File to define Bear class."""
__author__ = "730553137"

class Bear:

    # attributes
    age: int
    hunger_score: int
    
    def __init__(self, age_input: int = 0):
        self.age: int = age_input
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        self.age += 1
        # Increase age by 1
        return None