auction = []
def bidding(bid_name, bid_price):
    bid_name = input("What is your name? ")
    bid_price = int(input("What is your bidding price? $"))

bidding(bid_name, bid_price)
bid_continue = input("Do you want to continue bidding?(y or n) ")

game = True
while not game:
    if bid_continue == "y":
        bidding(bid_name, bid_price)
        print("\n" * 100)
        auction[bid_name] = bid_price
        max_key, max_value = max(auction.items(), key=lambda x: x[1])
        print(f"The winner is {max_key} with a bid of {max_value}")
