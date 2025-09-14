import random

MAX_SIDES = 1000
MAX_DICE = 100

# ASCII art for 6-sided dice
DICE_ART = {
    1: ("┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"),
    2: ("┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"),
    3: ("┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"),
    4: ("┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"),
    5: ("┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"),
    6: ("┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘")
}

def roll_dice():
    print("🎲 Welcome to the Dice Roller!")

    while True:
        try:
            sides_input = input(f"Enter the number of sides for the dice (default 6, max {MAX_SIDES}): ")
            sides = int(sides_input) if sides_input else 6
            if sides < 2:
                print("Dice must have at least 2 sides.")
                continue
            if sides > MAX_SIDES:
                print(f"Too high! Setting sides to {MAX_SIDES}.")
                sides = MAX_SIDES
        except ValueError:
            print("Please enter a valid integer.")
            continue

        try:
            num_input = input(f"How many dice do you want to roll? (default 1, max {MAX_DICE}): ")
            num_dice = int(num_input) if num_input else 1
            if num_dice < 1:
                print("You must roll at least 1 dice.")
                continue
            if num_dice > MAX_DICE:
                print(f"Too high! Setting number of dice to {MAX_DICE}.")
                num_dice = MAX_DICE
        except ValueError:
            print("Please enter a valid integer.")
            continue

        print("\nRolling... 🎲\n")
        results = [random.randint(1, sides) for _ in range(num_dice)]

        for i, result in enumerate(results, 1):
            print(f"Dice {i}: ", end="")
            if sides == 6:  # show ASCII only for 6-sided dice
                for line in DICE_ART[result]:
                    print(line)
            else:
                print(result)

        again = input("\nDo you want to roll again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    roll_dice()

