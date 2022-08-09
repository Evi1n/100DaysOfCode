logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bidders = []
bids = []

print("Welcome to the secret auction program!")

def info():
  name = input("What is your name?\n")
  bid = int(input("What's your bid?:\n$"))
  bidders.append(name)
  bids.append(bid)

  again = input("Are there any bidders? Type 'Y' for yes, type 'N' for no.")

  if again =="Y":
    info()

  elif again=="N":
    max_bid = bids[0]
    max_bidders = bidders[0]
    
    for i in range(len(bids)):
      if bids[i]>max_bid:
        max_bid = bids[i]
        max_bidders = bidders[i]
        
      else:
        max_bid = max_bid
        max_bidders = max_bidders
        
    print("The winner is {} with bid of ${}.".format(max_bidders, max_bid))

  else:
    print("Please type a invalid value!")
     
info()