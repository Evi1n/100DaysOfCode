logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print("Welcome to the calculator app!")

def add(num1, num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

 
def calculator():
    
    again = True

    while again:
        print(logo)
        num1 = int(input("What is the first number?"))
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        num2 = int(input("What is the second number?"))

        if operation == "+":
            print("{} + {} = {}".format(num1, num2, add(num1, num2)))
        elif operation == "-":
            print("{} + {} = {}".format(num1, num2, subtract(num1, num2)))
        elif operation == "*":
            print("{} + {} = {}".format(num1, num2, multiply(num1, num2)))
        elif operation == "/":
            print("{} + {} = {}".format(num1, num2, divide(num1, num2)))
        else:
            print("Please pick an valid operation!")
    

        again = input("Type 'Y' if you want to go again. Otherwise type 'N'.")

        if again == "Y":
            again = True
        elif again =="N":
            print("Good bye!")
            again = False
        else:
            print("Invalid value!")


calculator()

