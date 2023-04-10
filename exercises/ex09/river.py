"""File to define River class."""
__author__ = "730553137"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:

    # attributes
    day: int # tells what day of the river's lifecycle is being modeled
    bears: list[Bear] # stores the river's bear population
    fish: list[Fish] # stores the river's fish population
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

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

    def bears_eating(self):
        return None
    
    def check_hunger(self):
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
    
    def view_river(self):
        """Prints out the river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1
            # Incease day of the week by 1
        return None
