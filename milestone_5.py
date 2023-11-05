# Import the random module
import random 

# Define a class for hangman
class Hangman:
    '''
    This class is used to define the functions and attributes for Hangman game.

    Attributes:
        word_list(list): collection of words to be passed as a parameter.
        num_lives (int): the maximum number of attempts/guesses the user is allowed to make. Default value is set to 5.
        
    '''
    # Initialize the hangman object with word_list and num_lives
    def __init__(self, word_list, num_lives = 5):
        '''
        This function is used to guess the characters contained in a string.

        Args:
            word: The word to be guessed, picked randomly from the word_list. 
            word_guessed (list): a list of the letters of the word, with _ for each letter not yet guessed. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
            num_letters (int): the number of UNIQUE letters in the word that have not been guessed yet
            num_lives (int): the number of lives the player has at the start of the game.
            word_list (list): a list of words
            list_of_guesses (list): A list of the guesses that have already been tried. Set this to an empty list initially
        Returns:
            Date: the date created from the string.
        '''
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.num_lives = num_lives
        self.word_guessed = ["_" for each_letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    


    # Define the check_guess method
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Loop through the word and the word_guessed lists using enumerate
            for i, each_character in enumerate(self.word):
                # If the guess matches the letter in the word, replace the _ in the word_guessed list with the guess
                if each_character == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            # Reduce the num_lives by one
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


    # Define the ask_for_input method
    def ask_for_input(self):
        # Create a while loop and set the condition to True
        while True:
            guess = input("Guess a letter: ")
            # Check if the guess is NOT a single alphabetical character
            if not guess.isalpha() or len(guess) != 1:
                print( "Invalid letter. Please, enter a single alphabetical character.")
            # Check if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                print( "You already tried that letter!")
            else:
                # Call the check_guess method and pass the guess as an argument       
                self.check_guess (guess)
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
                break



# Define play_game function that will run all the code to run the game as expected
def play_game(word_list):
    num_lives = 5
   
    game =  Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            # Call the ask_for_input method to test the code
            game.ask_for_input()
        else:
            print("'Congratulations. You won the game!")
            print(f"The word is: {game.word_guessed}")
            break

# call your play_game function to play your game
words_to_guess = ["apple", "banana", "coconut"]
play_game(words_to_guess)









