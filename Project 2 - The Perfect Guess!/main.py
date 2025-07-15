import random

# Generate a random number between 1 and 100
n = random.randint(1, 100)

# Define the function to handle the number guessing game
def guess_number():
    # Initialize a global variable to count the number of guesses
    global Guesses 
    Guesses = 0
    
    # Start an infinite loop for the game
    while True:
        # Increment the guess counter
        Guesses += 1
        
        # Prompt the user to guess a number or exit the game
        guess = int(input("\nGuess a number between 1 and 99 (or -1 to exit): \n"))
        
        # Check if the user wants to exit the game
        if guess == -1:
            print("\nYou exited the game, The number was:\n", n)
            break
        
        # Check if the guessed number is lower than the target number
        elif guess < n:
            print("\nToo low, try again!")
        
        # Check if the guessed number is higher than the target number
        elif guess > n:
            print("\nToo high, try again!")
        
        # Check if the guessed number matches the target number
        elif guess == n:
            print(f"\nWOHOO! Congratulations, You guessed it right in {Guesses} guesses!\n")
            break
        
        # Handle invalid input (though this case is unlikely due to `int` conversion)
        else:
            print("\nInvalid input. Please enter a number between 1 and 99 or -1 to exit.\n")

# Call the function to start the game
guess_number()