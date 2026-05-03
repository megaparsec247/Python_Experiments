import random

logo = """ ________  ___  ___  _______   ________   ________  ___  ________   ________          ________  ________  _____ ______   _______
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\|\  \|\   ___  \|\   ____\        |\   ____\|\   __  \|\   _ \  _   \|\  ___ \
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|\ \  \ \  \\ \  \ \  \___|        \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \ \  \ \  \\ \  \ \  \  ___       \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \ \  \ \  \\ \  \ \  \|\  \       \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \ \__\ \__\\ \__\ \_______\       \ \_______\ \__\ \__\ \__\    \ \__\ \_______\
    \|_______|\|_______|\|_______|\_________\\_________\|__|\|__| \|__|\|_______|        \|_______|\|__|\|__|\|__|     \|__|\|_______|
                                 \|_________\|_________|

                                                                                                                                      """

random_integer = random.randint(1,100)

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

easy_attempts = 10
hard_attempts = 5
if choice == "easy":
    print("You have 10 attempts to make a guess")
    for i in range(10):
        user_choice = int(input("Make a guess: "))
        if user_choice > random_integer:
            print("Too high")
            print(f"Remaining guess: {easy_attempts - i}")
        elif user_choice < random_integer:
            print("Too low")
            print(f"Remaining guess: {easy_attempts - i}")
        else:
            print("You guessed it!")
            break

if choice == "hard":
    print("You have 5 attempts to make a guess")
    for _ in range(5):
        user_choice = int(input("Make a guess: "))
        if user_choice > random_integer:
            print("Too high")
            print(f"Remaining guess: {hard_attempts - i}")
        elif user_choice < random_integer:
            print("Too low")
            print(f"Remaining guess: {hard_attempts - i}")
        else:
            print("You guessed it!")
            break
