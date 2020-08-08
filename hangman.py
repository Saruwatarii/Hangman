import random

print("H A N G M A N")

guessing_word = random.choice(['python', 'java', 'kotlin', 'javascript'])

# How long the word is, minus the first 3 letters
length = len(guessing_word)
# Multiple the length with "-" for hide the right word
# hidden = "-" * length
hidden = "-" * len(guessing_word)
# Add the three first visible letters and then the hidden ones.

# Let the user  see the hint before typing
# user_guess = input("Guess the word: " + hint + " ").lower()
# A list containing letters the user have guessed which not in the hidden word.
already_used = []
game_over = 0
tries = 8
flag = True
while flag:
    print('Type "play" to play the game, "exit" to quit')
    player = input().lower()
    if player == "play":

        while tries != game_over:
            print()
            print(hidden)
            user_guess = input("Input a letter: ")

            if len(user_guess) != 1:
                print("You should input a single letter")
                continue

            if not user_guess.islower():
                print("It is not an ASCII lowercase letter")
                continue

            if guessing_word == hidden:
                print(f"{guessing_word}\nYou guessed the word!\nYou survived!")
                guessing_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
                hidden = "-" * len(guessing_word)
                already_used.clear()
                break
            # Check whether the letter is in the hidden word and is in the already_used list, if not in both, it gets added to the list
            if (user_guess not in guessing_word) and (user_guess not in already_used):
                print("No such letter in the word")
                already_used.append(user_guess)
                tries -= 1
                continue

            if user_guess in already_used:
                print("You already typed this letter")
                # tries -= 1
                continue

            if user_guess not in guessing_word:
                print("No such letter in the word")
                tries -= 1
                continue

            if user_guess in hidden:
                print("No improvements")
                tries -= 1
                continue

            elif user_guess in guessing_word:
                temp = list(hidden)
                for i in range(len(guessing_word)):
                    if guessing_word[i] == user_guess:
                        temp[i] = guessing_word[i]
                        hidden = "".join(temp)
                continue
        else:
            print("You are hanged!")
            tries = 8

            guessing_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
            hidden = "-" * len(guessing_word)
            already_used.clear()

    elif player == "exit":
        flag = False
    else:
        print("You did not enter 'play' or 'exit, so i will ask you again.")
        flag
