import random

fun_words = ['dog','cow', 'cat' ]
King_word = random.choice(fun_words)

word_style = ['_'] * len(King_word)

word_found = False

Attempts = 0

max_attempts = 5


print("WELCOME TO HANGMAN")
print("FIND THE KING WORD AND WIN!")
print("\n")


while not word_found and Attempts < max_attempts:

    Hit_word = input("Enter a letter to find the KING word: ").lower()
    print("\n")

    if len(Hit_word) != 1 or not Hit_word.isalpha():
        print("Please enter only one letter.")
        print("\n")
        continue

    if Hit_word in King_word:

        for i in range(len(King_word)):

            if King_word[i] == Hit_word:
                word_style[i] = Hit_word

        print("Spot on! You found a letter.")
        print("Word:", ' '.join(word_style))
        print("___________________________________________")
        print("\n")

    else:
        Attempts += 1
        print("Wrong!!")
        print("Attempts:", Attempts)
        print("___________________________________________")
        print("\n")

    if '_' not in word_style:
        word_found = True
        print("Congratulations! You own the KING word:", King_word)
        print("___________________________________________")
        print("\n")

if not word_found:
    print("Game Over! The KING word was:", King_word)
