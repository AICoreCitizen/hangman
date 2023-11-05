import random 

def check_guess(guess):
    guess = guess.lower()
    word_list = ["Banana", "Orange", "Mango", "Kiwi", "Tomato"]
    word = random.choice(word_list)
    print(f"The word selected is: {word}")
    if guess in word:
        print(f"Good guess! {guess} is in the word {word}.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print( "Invalid letter. Please, enter a single alphabetical character.")
    check_guess (guess)

ask_for_input()



