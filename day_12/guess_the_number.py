from random import randint
from replit import clear

logo = """
 _______                                _                                _                 
(_______)                           _  | |                              | |                
 _   ___ _   _ _____  ___  ___    _| |_| |__  _____    ____  _   _ ____ | |__  _____  ____ 
| | (_  | | | | ___ |/___)/___)  (_   _)  _ \| ___ |  |  _ \| | | |    \|  _ \| ___ |/ ___)
| |___) | |_| | ____|___ |___ |    | |_| | | | ____|  | | | | |_| | | | | |_) ) ____| |    
 \_____/|____/|_____|___/(___/      \__)_| |_|_____)  |_| |_|____/|_|_|_|____/|_____)_|    
                                                                                       
"""
 
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    choise = input("Choose a difficulty. Type 'easy' for easy, type 'hard' for hard.")
    answer = randint(1, 100)

    if choise == 'easy':
        attempts = 10
    else:
        attempts = 5

    while attempts >= 1:
        print("You have {} attempts remaining to guess the number".format(attempts))
        guess = int(input("Make a guess: "))

        if guess == answer:
            if attempts>=0:
                print("You got it! The answer is {}".format(answer))
        elif guess > answer:
            attempts -=1
            if attempts > 0:
                print("Too high.\nGuess again.")
            else:
                print("You've run out of the guesses. You lose!")
        elif guess < answer:
            attempts -=1
            if attempts>0:
                print("Too low.\nGuess again.")
            else:
                print("You've run out of the guesses. You lose!")
    
    again = input("Do you want to play again? Type 'Y' for yes, type 'N' for no.")
    if again == 'Y':
        clear()
        game()
    else:
        print("Good bye!")

game()