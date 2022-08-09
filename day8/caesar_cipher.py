logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
print("Welcome to the caesar cipher!")

def play():
    def caesar_encyrpted(message, key):
        encrypted_message = ''
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in message:
            encrypted_message += alphabet[(alphabet.index(i)+shift) % len(alphabet)]
        print(encrypted_message)

    def caesar_cyrpted(message, key):
        crypted_message = ''
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in message:
            crypted_message += alphabet[(alphabet.index(i)-shift) % len(alphabet)]
        print(crypted_message)

    choise = input("What do you want to do? Encyrpt or crypted? Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if choise == "encode":
        shift = int(input("Type the shift number:\n"))
        message = input("Type your message:\n")
        #encyrpted_message = caesar_encyrpted(message, shift)
        print("Here's the encoded result:")
        caesar_encyrpted(message, shift)
    elif choise == "decode":
        shift = int(input("Type the shift number:\n"))
        message = input("Type your message:\n")
        #cyrpted_message = caesar_cyrpted(message, shift)
        print("Here's the decode result:")
        caesar_cyrpted(message, shift)

    again = input("Type 'Y' if you want to go again. Otherwise type 'N'.")

    if again == "Y":
        play()
    elif again == "N":
        print("Good bye!")
    else:
        print("Please type a valid letter!")

play()




