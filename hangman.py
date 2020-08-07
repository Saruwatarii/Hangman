import random

print("H A N G M A N")
print("Under construction.")

guessing_word = random.choice(['python', 'java', 'kotlin', 'javascript'])

show_three_letter = guessing_word[:3]
# How long the word is, minus the first 3 letters
length = len(guessing_word) - len(show_three_letter)
# Multiple the length with "-" for hide the right word
 # hidden = "-" * length
hidden =  "-" * len(guessing_word)
# Add the three first visible letters and then the hidden ones.
hint = show_three_letter + hidden
# Let the user  see the hint before typing
# user_guess = input("Guess the word: " + hint + " ").lower()
game_over = 0
tries = 8
while tries != game_over:
    print()
    print(hidden)
    user_guess = input("Input a letter: ").lower()

    if guessing_word == user_guess:
        print("You survived!")

    elif user_guess not in guessing_word:
        print("No such letter in the word")
        tries -= 1
        continue

    elif user_guess in guessing_word:
        temp = list(hidden)
        for i in range(len(guessing_word)):
            if guessing_word[i] == user_guess:
                temp[i] = guessing_word[i]
                hidden = "".join(temp)

        tries -= 1
        continue

else:
    print()
    print("Thanks for playing!\nWe'll see how well you did in the next stage")
