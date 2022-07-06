import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))

if user_choice-1 >= 3 or user_choice-1 < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(images[user_choice-1])

    computer_choice = random.randint(1, 3)
    print("Computer chose:")
    print(images[computer_choice])

    if user_choice == 1 and computer_choice == 2:
        print("You win!:)")
    elif computer_choice == 1 and user_choice == 2:
        print("You lose:(")
    elif computer_choice+1 > user_choice:
        print("You lose:(")
    elif user_choice > computer_choice+1:
        print("You win!:)")
    elif computer_choice == user_choice:
        print("It's a draw:|")

    