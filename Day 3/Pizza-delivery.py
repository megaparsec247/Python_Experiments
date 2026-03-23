print("Welcome to Python Pizza Delivery.")
total = 0

size = input("What size pizza do you want? S, M, L: ")

if (size == "S"):
    total += 15

elif (size == "M"):
    total +=20

else:
    total +=25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if (pepperoni == "Y"):
    if size == "S":
        total+=2
    else:
        total+=3

cheese = input("Do you want extra cheese? Y or N: ")

if (cheese == "Y"):
    total +=1

print(f"Total bill:${total}")