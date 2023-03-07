"""EX06 - Taking care of my plant!"""
__author__ = "730553137"

WATER_EMOJI: str = "\U0001F4A7"
FIRE_EMOJI: str = "\U0001F525"
PLANT_EMOJI: str = "\U0001F331"


def main() -> None:
    greet()
    
    global points
    points: int = 0
    
    global player
    player: str = ""


def greet(player: str) -> None:
    print(f"Welcome to my {PLANT_EMOJI} garden game!")
    player: str = input("What's your name? ")
    print(f"Hello {player}! I hope you're ready to take care of your plant!")


def first_option(points: int):
    print(f"You picked the end game option. Goodbye! You accumulated {points} adventure points.")


def second_option(points: int):
    print(f"You picked the second option. You get to {WATER_EMOJI} water your plant. Your plant is happy!")
    points += 5


def third_option(points: int):
    print(f"You picked the third option. You set one of your plants leaves on {FIRE_EMOJI} fire. Your plant is not happy!")
    points -= 5

if __name__ == "__main__":
    main()