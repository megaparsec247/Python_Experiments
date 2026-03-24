import random

word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)

placeholder = ""
word_length= len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"Number of lives left: {lives}")

    guess = input("Guess a letter: ").lower()

    display = ""

    if guess in correct_letters:
        print("You have already guessed this letter.")

    for letter in chosen_word:
            if(letter == guess):
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"       
    print(display)

    if guess not in chosen_word:
        lives -=1
        print("Incorrect guess.")
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You win.")