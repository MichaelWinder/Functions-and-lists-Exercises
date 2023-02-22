item = input("What is auction for? ").capitalize()
reserve = float(input("What is the reserve price? "))
highest_Bid = 0
bid = 0
while bid != -1:
    bid = float(input(f"\nHighest bid so far is ${highest_Bid}\nWhat is your "
                      f"bid? "))
    if bid > highest_Bid:
        highest_Bid = bid
    elif bid <= highest_Bid:
        print("Please enter a higher bid")
if highest_Bid >= reserve:
    print(f"\nThe auction for the {item} finished with a bid of "
          f"${highest_Bid}")
else:
    print("Highest bid did not reach the reserve")
