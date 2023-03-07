"""EX06 - Taking care of my plant!"""
__author__ = "730553137"

def main() -> None:
    print("Welcome to my program!")
    
    global points
    points: int = 0
    
    global player
    player: str = ""


def greet(player) -> None:
    print(f"Hello {player}, welcome to my garden!")


def first_option(total):
    print(f"You picked the end option. Goodbye! You accumulated {total} adventure points.")


def second_option():
    print("You picked the second option. You are headed to the garden to choose an already grown plant!")


def third_option():
    print("You picked the third option. You are headed to the store to get seeds and start from scratch!")


if __name__ == "__main__":
    main()