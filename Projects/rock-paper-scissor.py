import random

print("Welcome to Rock-Paper-Scissors")
user = int(input(("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")))

# random = random.randint(0,2)

# if (random == user):
#     print("Draw")

# elif(random == 0 and user == 1):
#     print("You win")

# elif(random == 1 and user == 0):
#     print("You lose")

# elif(random == 1 and user == 2):
#     print("You win")

# elif(random == 2 and user == 1):
#     print("You lose")

# elif(random == 0 and user == 2):
#     print("You lose")

# elif(random == 2 and user == 0):
#     print("You win")

if user not in [0,1,2]:
    print("Invalid input")
    exit()

computer = random.randint(0,2)

print(f"Computer chose: {computer}")

if user == computer: 
    print("Draw")

elif (user == 0 and computer == 2) or \
    (user == 1 and computer == 0) or \
    (user == 2 and computer == 1):
    print("You win")
else:
    print("You lose")