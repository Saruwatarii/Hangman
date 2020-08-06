

import random


print("H A N G M A N")
print("Under construction.")

guessing_word = random.choice(['python', 'java', 'kotlin', 'javascript'])

show_three_letter = guessing_word[:3]
# How long the word is, minus the first 3 letters
length = len(guessing_word) - len(show_three_letter)
# Multiple the length with "-" for hide the right word
hidden = "-" * length
# Add the three first visible letters and then the hidden ones.
hint = show_three_letter + hidden

# Let the user  see the hint before typing
user_guess = input("Guess the word: " + hint + " ").lower()

if guessing_word == user_guess:
    print("You survived!")
else:
    print("You are hanged!")


