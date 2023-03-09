"""EX06 - Taking care of my plant!"""
__author__ = "730553137"

import random

WATER_EMOJI: str = "\U0001F4A7"
FIRE_EMOJI: str = "\U0001F525"
PLANT_EMOJI: str = "\U0001F331"

points: int = 0
player: str = ""


def main() -> None:
    """Defines the main function which asks the player to choose an option and tells them how many points they have."""
    global points
    global player 

    greet(player) 

    while True:
        print(f"You have {points} points!")
        new_choice: str = input(f"Would you like to continue with {points} points or pick the first_option, second_option, or third_option? ")

        if new_choice == "first_option":
            points = first_option(points, player)
        elif new_choice == "second_option":
            points = second_option(points)
        elif new_choice == "third_option":
            points = third_option(points)
        return points


def greet(player: str) -> None:
    """Defines the greet function which welcomes the player to the game and asks for their name."""
    print(f"Welcome to my {PLANT_EMOJI} garden game!")
    player: str = input("What's your name? ")
    print(f"Hello {player}! I hope you're ready to take care of your plant!")

 
def first_option(points: int, player: str) -> int:
    """Defines the first_option function which is the end game option that gives the player a chance to earn random bonus points."""
    random_points: int = random.randint(1, 5)
    points += random_points
    print(f"You picked the end game option. You accumulated {points} adventure points throughout the game, with the addition of {random_points} bonus points from luck. Goodbye {player}!")
    return points


def second_option(points: int) -> int:
    """Defines the second_option which gives the player a chance to earn or lose points based on taking care of the plant."""
    print(f"You picked the second option. You get to {WATER_EMOJI} water your plant. Your plant is happy!")
    points += 5
    while True:
        too_much_water: str = input(f"You added a bit too much water {player}, would you like to put the plant in the sun to dry some of it up? (yes or no)")
        if too_much_water == "yes":
            print(f"You put the {PLANT_EMOJI} plant in the sun and it soaked up the water!")
            points += 5
        elif too_much_water == "no":
            print(f"You did not put the {PLANT_EMOJI} plant in the sun and it wilted from all the water.")
            points -= 5
        return points


def third_option(points: int):
    """Defines the third_option which gives the player a chance to earn or lose points based on taking care of the plant."""
    print(f"You picked the third option. You set one of your plants leaves on {FIRE_EMOJI} fire. Your plant is not happy!")
    points -= 5
    while True:
        add_water: str = input(f"Would you like to add {WATER_EMOJI} water to the plant, {player}? (yes or no)")
        if add_water == "yes":
            print(f"You added {WATER_EMOJI} water, now the plant is happy!")
            points += 5
        elif add_water == "no":
            print(f"You did not add water {FIRE_EMOJI}. The plant is dead.")
            points -= 5


if __name__ == "__main__":
    main()