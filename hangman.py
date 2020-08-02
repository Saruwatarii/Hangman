import random


print("H A N G M A N")
print("Under construction.")

guessing_word = random.choice(['python', 'java', 'kotlin', 'javascript'])

user_guess = input("Guess the word: ").lower()

if guessing_word == user_guess:
    print("You survived!")
else:
    print("You are hanged!")
