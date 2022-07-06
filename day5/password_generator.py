import random
print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'X', 'W', 'Y', 'Z']

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+" , "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",  "[",  "]", "^",  "_", "{", "|", "}", "~"]

num_letters = int(input("How many letters would you like in your password?\n"))
num_nums = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []
total_character = num_letters + num_nums + num_symbols

for i in range(num_letters):
    password_list.append(random.choice(letters))

for i in range(num_nums):
    password_list.append(random.choice(numbers))

for i in range(num_symbols):
    password_list.append(random.choice(symbols))


password = "".join(random.sample(password_list, total_character))

print("Here is your Password: {}".format(password))