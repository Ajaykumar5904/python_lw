# number-guessing-game.py

import random

#login
users = {"admin": "1234"}  

def signup():
    username = input("Username: ")
    password = input("Password: ")
    users[username] = password
    print("Account created!")

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    if users.get(username) == password:
        print("Login successful!")
        return True
    else:
        print("Wrong credentials!")
        return False


#main code

def play_game():
    # Initialize counters for high, low, and win
    high = 0
    low = 0
    win = 0

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    #print(number)
    

    while win == 0:
        try:
            # Ask the user to input a guess
            userNum = int(input("Please guess a number between 1 and 100: "))

            # Check if the user's guess is too high, correct, or too low
            if userNum > number:
                message = "Too high, try again."
                high += 1
            elif userNum == number:
                message = "You got it correct! Congratulations!"
                win += 1
                break
            else:
                message = "Too low, try again."
                low += 1

            # Print the appropriate message
            print()
            print(message)
            print()

        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

    # Display the total number of guesses
    print()
    print("Number of times too high:", high)
    print("Number of times too low:", low)
    print("Total number of guesses:", high + low + win)


# -------- Play Again Feature --------
def main():
    while True:
        print("1. Signup  2. Login  3. Quit")
        choice = input("Choose: ")
    
        if choice == "1":
            signup()
        elif choice == "2":
            if login():
                break
        elif choice == "3":
            print("Bye!")
            break

        play_game()
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("\nThanks for playing! 👋")
            break


# Start the game
main()
