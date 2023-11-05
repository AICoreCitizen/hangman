# Hangman


### Table of Contents
1. [Project Description](#project-description)
2. [Usage Instructions](#usage-instructions)
3. [File Structure of the Project](#file-structure-of-the-project)
4. [License Information](#license-information)
<!--  - [Subsection 1.1](#subsection-1.1) 
    - [Subsection 1.2](#subsection-1.2)-->
## Project Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Usage Instructions

### Run Two Functions to Check User Input
There are two functions in this code are now contained in a class called Hangman.  The ask_for_input function prompts the user for an input of an alphabetical character, then Iteratively check if the input is a valid guess. The second function called check_guess passes in the variable guess as a parameter for the function to check if the guess is a randomly chosen word from a list.

_Note: to capture occurence of words with repeated characters such as coconut in check_guess method, enumerate function was used to capture both the index and the value of each item in a list. For example, enumerate(self.word) will return something like [(0, 'c'), (1, 'o'), (2, 'c'), (3, 'o'), (4, 'n'), (5, 'u'), (6, 't')]. This way, we can loop through both the index and the letter of the word, and replace the corresponding _ in the word_guessed list if the guess matches the letter._

## File Structure of the Project
To be updated soon
## License Information
To be updated soon