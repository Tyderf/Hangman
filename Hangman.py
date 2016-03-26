# 6.00 Problem Set 3
#
# Hangman
#
# 2. The game must be interactive: let a player know how many letters the word contains and ask the user to supply guesses.
# The user should receive feedback immediately after each guess.
# Display to the user the partially guessed word so far,
# as well as either the letters that the player has already guessed or
# letters that the player has yet to guess.


# 3. A player is allowed some number of guesses. Once you understand how the game works,
# pick a number that seems reasonable to you. Make sure to remind the player of how
# many guesses they has left after each turn.


# 4. A player loses a guess only when s/he guesses incorrectly.


# 5. The game should end when the player constructs the full word or runs out of guesses. If
# the player runs out of guesses they lose, reveal the word to the player when the game ends.
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

import random
import sys
import time
import string

WORDLIST_FILENAME = "words.txt"

typing_speed = 15  # wpm
# your code begins here!

# 1. Select a word at random from the list of available words provided in words.txt.
# The functions for loading the word list and selecting a random word have already been provided for you in ps2_hangman.py.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]


def slow_type(whatYouWantToType):
    for character in whatYouWantToType:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(random.random() * 1.0 / typing_speed)
    print('')
    return ''


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)




def get_guess(guesses, newAvailableLetters, correctGuesses):
    if guessesLeft >= 1 and guessedWord == chosenWord:
        print('')
        print('')
        print("VICTORY")
        print("The word was: ", chosenWord)
        sys.exit(0)
    print('')
    print("You have" + ' ' + str(guesses) + ' ' + "guesses left.")
    print("Available letters: " + ' ' + newAvailableLetters)
    print("Letters:  " + blankGuessSeparator.join(correctGuesses))
    print("Please guess a letter: ", end='')
    return input()


def ignore_duplicate_guesses(guesses, newAvailableLetters):
    print("     You can not guess that letter.")
    print("     Letters: ", newAvailableLetters)


# end of helper code
# -----------------------------------
# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# printGuesses = "8"
chosenWord = choose_word(wordlist)


def get_unique_letters_in_word():
    uniqueLettersInWord = []
    for duplicates in chosenWord:
        if duplicates not in uniqueLettersInWord:
            uniqueLettersInWord.append(duplicates)

    return uniqueLettersInWord


uniqueLettersInChosenWord = get_unique_letters_in_word()

guesses = len(uniqueLettersInChosenWord) + 8
# Set the guesses to the length of the chosen word without duplicate letters and add 5
allGuesses = []
allCorrectGuesses = []
correctGuesses = []
duplicate = []
blankGuessSeparator = ' '

# Greeting
print(">" + ">" + ">")
print("Welcome to the game, Hangman!")
# Tell player how many letters are in the word
# Tell the player how many guesses they have left
# Tell player the available letters
for letter in chosenWord:
    correctGuesses.append("_")
    blankGuessSeparator.join(correctGuesses)

# Given the word that was chosen, create a blank set that can contain the user's guesses in the order in which they appear in the chosen word

print("I am thinking of a word that is" + ' ' + str(len(chosenWord)) + ' ' + "letters long.")
print("=============")
print('')
newAvailableLetters = ''.join(letters)

for turn in range(guesses):

    allCorrectGuesses2 = allCorrectGuesses.append(correctGuesses)
    guessedWord = ''.join(correctGuesses)

    # Got the guess
    numberOfGuesses = guesses - turn
    guessesLeft = numberOfGuesses - 1
    guess = get_guess(numberOfGuesses, newAvailableLetters, correctGuesses)
    findGuess = newAvailableLetters.find(guess)

    if findGuess not in chosenWord:
        ignore_duplicate_guesses(guesses, newAvailableLetters)
        if guessesLeft < 1 and guessedWord != chosenWord:
            print("GAME OVER, Ending game in 5 seconds...")
            print("The word was: ", chosenWord)
            time.sleep(5)
            sys.exit(0)


    elif guess in chosenWord:
        duplicate.append(guess)
        allGuesses.append(guess)
        allCorrectGuesses.append(correctGuesses)
        if guessesLeft < 1 and guessedWord != chosenWord:
            print("GAME OVER, Ending game in 5 seconds...")
            print("The word was: ", chosenWord)
            time.sleep(5)
            sys.exit(0)
        print("Oops! That letter wasn't in the word.")
        # Compare the guessed word with the actual word. If they match, then victory
        if guessesLeft >= 1 and guessedWord == chosenWord:
            print('')
            print('')
            print("VICTORY, Ending game in 5 seconds...")
            print("The word was: ", chosenWord)
            time.sleep(5)
            sys.exit(0)
        letterIndex = 0
        newAvailableLetters = ""

        while (letterIndex != None):
            # Wherever the letter occurs in the word,
            # we replace the underscore at the same index in the blankSet
            try:
                letterIndex = chosenWord.index(guess, letterIndex)
                correctGuesses[letterIndex] = guess
                letterIndex = letterIndex + 1
            except Exception:
                letterIndex = None
        if guess in chosenWord:
            print("Good Job! Letters: ", blankGuessSeparator.join(correctGuesses))
        else:
            print("Letters: ", blankGuessSeparator.join(correctGuesses))
        letters = [x for x in letters if x != guess]
        newAvailableLetters = ''.join(letters)

        print('')


    else:
        if guessesLeft < 1 and guessedWord != chosenWord:
            print("GAME OVER, Ending game in 5 seconds...")
            print("The word was: ", chosenWord)
            time.sleep(5)
            sys.exit(0)
        print("Oops! That letter wasn't in the word.")

        letters = [x for x in letters if x != guess]
        newAvailableLetters = ''.join(letters)
        allGuesses.append(guess)

        print('')
