# imports the random module
import random

# computer randomly chooses an option
computer = random.choice( [0, 1, 2])

# asks the user for their choice
youchoice = input("Enter your choice \"S: Snake, W: Water, G: Gun\" : ").lower()

# dictionary to convert user's choice to a number
youdict = {"s": 0, "w": 1, "g": 2}

# dictionary to convert a number to the user's choice
reversedict = {0: "Snake", 1: "Water", 2: "Gun"}

# converts the user's choice to a number
you = youdict[youchoice]

# prints the user's and computer's choices
print(f"You chose {reversedict[you]}, the computer chose {reversedict[computer]}")

# checks if the user and computer have the same choice
if you == computer:
    print ('It is a draw')

# checks all the possible winning combinations
else:
    if you == 0 and computer == 1:
        print ('You win')
    elif you == 1 and computer == 2:
        print ('You win')
    elif you == 2 and computer == 0:
        print ('You win')
    else:
        print ('You lose')  