import random
import string

WORDLIST_FILENAME = "palavras.txt"

"""
Depending on the size of the word list, this function may
take a while to finish.
"""

def validateFileInput():
    try:
        with open(WORDLIST_FILENAME) as file:
            print "Loading word list from file..."
            if (checkIfIsEmpty()):
                if (checkIfWordsAreValid(checkIfIsEmpty()) == 0):
                    hangman(choosesWordRandomly(checkIfIsEmpty()))
                else:
                    print"Error: File contains invalid words."
            else:
                print"Error: File is empty."

            pass
    except IOError as e:
        print "Error: Unable to open file " + WORDLIST_FILENAME + '. File does not exist or you don\'t have ' \
                                                                  'permissions to open the file.'


def checkIfWordsAreValid(wordlist):
    numberOfInvalidWords = 0
    for word in wordlist:
        if (not word.isalpha()):
            print "Warning: Invalid word: " + word
            numberOfInvalidWords = numberOfInvalidWords + 1
        if (len(word) < 2 or len(word) > 46):
            print "Warning: Invalid word: " + word
            numberOfInvalidWords = numberOfInvalidWords + 1

    return numberOfInvalidWords


def checkIfIsEmpty():
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline().lower()

    if (string.split(line)):
        return string.split(line)


def choosesWordRandomly(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True


def getGuessedWord():
    guessed = ''
    return guessed


def getAvailableLetters(lettersGuessed):
    import string
    # string.ascii_lowercase = abcdefghijklmnopqrstuvwxyz
    available = string.ascii_lowercase
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
    print 'Available letters', available
    return available


def letterIsInLettersGuessed(letter, lettersGuessed, secretWord):
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print 'Oops! You have already guessed that letter: ', guessed


def letterIsInSecretWord(letter, lettersGuessed, secretWord):
    lettersGuessed.append(letter)
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'
    print 'Good Guess: ', guessed


def welcome(secretWord):
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

def validateInputLetter(letter, availableLetters):
    if(not letter or len(letter) > 1):
        print"Warning:", letter ," is not a letter."
        return False
    elif (not letter.isalpha()):
        print"Warning:", letter ," is not a valid letter."
        return False
    elif(not letter in availableLetters):
        print"Warning: You already try the letter:", letter, "."
        return False
    else:
        return True


def chooseLetter(guesses, lettersGuessed, secretWord):
    print 'You have', guesses, 'guesses left.'
    availableLetters = getAvailableLetters(lettersGuessed)
    isThisLetterValid = False
    while(not isThisLetterValid):
        letter = raw_input('Please guess a letter: ')
        isThisLetterValid = validateInputLetter(letter, availableLetters)
    if letter in lettersGuessed:
        letterIsInLettersGuessed(letter, lettersGuessed, secretWord)
    elif letter in secretWord:
        letterIsInSecretWord(letter, lettersGuessed, secretWord)
    else:
        guesses -= 1
        lettersGuessed.append(letter)
        guessed = getGuessedWord()
        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_'
        print 'Oops! That letter is not in my word: ', guessed
    print '------------'
    return guesses


def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    welcome(secretWord)
    while isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        guesses = chooseLetter(guesses, lettersGuessed, secretWord)
    else:
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was', secretWord,'.'


validateFileInput()
