import random

# Define a function to simulate a dice roll
def roll_dice(num_dice, dice_type):
    total = 0
    rolls = []
    for i in range(num_dice):
        roll = random.randint(1, dice_type)
        total += roll
        rolls.append(roll)
    return (rolls, total)

# Define the main function
def main():
    # Define the available dice types
    dice_types = ["d2", "d4", "d6", "d8", "d10", "d12", "d20", "d100"]

    # Prompt the user to select the dice type and the number of dice to roll
    print("Welcome to the Advanced Dice Rolling Simulator!")
    dice_type = input("Please select a dice type: " + ", ".join(dice_types) + "\n")
    num_dice = int(input("Please enter the number of dice to roll: "))

    # Extract the number of sides from the selected dice type
    dice_sides = int(dice_type[1:])

    # Simulate the dice rolls and display the results
    rolls, total = roll_dice(num_dice, dice_sides)
    print("You rolled: " + ", ".join(str(r) for r in rolls))
    print("Total: " + str(total))

# Call the main function
if __name__ == '__main__':
    main()
