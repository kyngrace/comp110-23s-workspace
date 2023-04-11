"""File to define River class."""
__author__ = "730553137"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Declares the class River."""

    # attributes
    day: int  # tells what day of the river's lifecycle is being modeled
    bears: list[Bear]  # stores the river's bear population
    fish: list[Fish]  # stores the river's fish population
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def remove_fish(self, amount: int) -> None:
        """Remove a certain (the frontmost) fish from the the river."""
        idx: int = 0
        while idx < amount and self.fish:
            self.fish.pop(0)
            idx += 1

    def check_ages(self):
        """Check for the ages of bears and fish in the river and get rid of the ones that are too old."""
        # Check for fish that are too old and remove them if they are a certain age
        young_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                young_fish.append(fish)
        self.fish = young_fish

        # Check for the bears that are too old and remoce them if they are a certain age
        young_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                young_bears.append(bear)   
        self.bears = young_bears    
        return None

    def bears_eating(self, bears: list[Bear]):
        """Puts controls on how many fish a bear will eat when there is a certain amount in the river."""
        for bear in bears:
            if self.num_fish >= 5:
                bear.eat(3)
            else:
                bear.eat(0)
        return None
    
    def check_hunger(self):
        """Checks the hunger scores of the bears in the river and if a score is less than zero then it removes the bear from the river."""
        living_bears: list[Bear] = []
        for bear in self.bears:
            bear.one_day()
            if bear.hunger_score >= 0:
                living_bears.append(bear)
        self.bears = living_bears
        # Updates the original bear list to be equal to the living bears list
        return None
        
    def repopulate_fish(self):
        """Produces 4 baby fish per every fish pair."""
        # Produces a fish offspring from a 2 fish pair
        num_fish = self.num_fish
        baby_fish: list[Fish] = (num_fish // 2) * 4
        self.num_fish += baby_fish
        return None
    
    def repopulate_bears(self):
        """Produces 1 bear cub per every bear pair."""
        # Produces a bear offspring from a 2 bear pair
        num_bears: int = len(self.bears)
        baby_bears: list[Bear] = []
        for idx in range(num_bears // 2):
            bear_one = self.bears[idx * 2]
            bear_two = self.bears[idx * 2 + 1]
            bear_offspring = Bear()
            baby_bears.append(bear_offspring)
        for bear in baby_bears:
            self.bears.append(bear)
        return None
    
    def view_river(self):
        """Prints out the river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        day: int = 0
        while day <= 7:
            self.one_river_day()
            day += 1
            # Incease day of the week by 1
        return None
