import random
from game_data import data
from replit import clear

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def random_account():
    return random.choice(data)

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():

    print(logo)
    score = 0
    game_status = True
    account_a = random_account()
    account_b = random_account()
    
    while game_status:

        account_a = account_b
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print("Compare A: {}.".format(format_data(account_a)))
        print(vs)
        print("Against B: {}.".format(format_data(account_b)))

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        clear()
        print(logo)

        if is_correct:
            score +=1
            print("You're right! Current score: {}.".format(score))
        else:
            game_status = False
            print("Sorry, that's wrong. Final score: {}".format(score))

game()