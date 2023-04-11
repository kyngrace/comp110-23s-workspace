"""File to define Bear class."""
__author__ = "730553137"


class Bear:
    """Declares the class Bear."""

    # attributes
    age: int
    hunger_score: int
    
    def __init__(self, age_input: int = 0):
        """Declares the __init__ function to begin keeping track of age and hunger_score of bears."""
        self.age: int = age_input
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        """Declares the one_day function to increase the age and decrease the hunger_score."""
        self.age += 1
        # Increase age by 1
        self.hunger_score -= 1
        # Decrease hunger_score by 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Increases the bears hunger_score by how many fish the bear eats."""
        self.hunger_score += num_fish