# Dice Rolling Simulator Program

# LOGIC BUILDING
# 1. Generate random numbers between 1 to 6
# 2. Use conditional statements to check user input
# 3. Use loop so user can roll dice multiple times

import random # random module is used to generate random numbers
import time  # time module is used to create delay for better animation effect

# Dice faces using ASCII(American Standard Code for Information Interchange) art
DICE_FACES = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}
# Function to roll the dice
def dice_roll():
    return random.randint(1,6)  # randint(1,6) generates a random number between 1 and 6
# Main function that controls the simulator
def dice_simulator():
    # Display welcome message to the user
    print("🎲 Welcome to the Dice Rolling Simulator! 🎲")
    print("Type 'yaa' to roll the dice or 'done' to Exit.")
    print()

    while True: # Infinite loop so the program keeps running until user exits
        # Taking input from the user
        # lower() converts input to lowercase
        # strip() removes extra spaces
        ask_user = input("Your input: ").lower().strip() 
         
         # If user types yaa → roll the dice
        if ask_user == "yaa":
            for _ in range(4):# Small animation effect before showing result
                print("🎲", end=" ")
                time.sleep(0.5) # wait for half second
            print()

            # Call dice_roll() function to generate random number
            result = dice_roll()
            # show the number
            print(f"👉 You rolled: {result}")
             # print the dice design
            for line in DICE_FACES[result]:
             print(line)
            print()

            # If user types done → exit the program
        elif ask_user == "done":
            print("Thanks for playing!👋")
            break
        # If user enters anything else → show error message
        else:
            print("❌ Please type 'yaa' to roll the dice or 'done' to Exit.❌")
            print()
# This ensures the program runs only when this file is executed directly
dice_simulator()