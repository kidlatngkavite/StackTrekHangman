# Import Libraries
from random import choice
from threading import Timer


# Initialize Variables


lettersGuessedList = []
lettersGuessedDisplay = ""
wrongCount = 0
rightCount = 0

# input timeout
inputTime = 10
maxWrongGuess = 7

"""add new word to the list below"""

wordList = ["APPLE", "BANANA", "CHERRY", "DURIAN", "EGGPLANT"]


playAgain = "Y"

# drawing the hangman
drawingHang = ["  _______\n |       |\n         |\n         |\n         |\n         |\n         |",
               "  _______\n |       |\n O       |\n         |\n         |\n         |\n         |",
               "  _______\n |       |\n O       |\n |       |\n         |\n         |\n         |",
               "  _______\n |       |\n O       |\n/|       |\n         |\n         |\n         |",
               "  _______\n |       |\n O       |\n/|\\      |\n         |\n         |\n         |",
               "  _______\n |       |\n O       |\n/|\\      |\n |       |\n         |\n         |",
               "  _______\n |       |\n O       |\n/|\\      |\n |       |\n/        |\n         |",
               "  _______\n |       |\n 0       |\n/|\\      |\n |       |\n/ \\      |\n         |"]


# function Declarations

""" function to get user input
    get usr input and return it"""


def getUserInput():
    userInput = input("Choose a letter: ")
    return userInput


""" function to handle user input timeout
    use global variable wrongcount to treat
    timeout as an invalid input"""


def timeout():
    global wrongCount
    wrongCount += 1
    print("Timeout")
    # print(f"{wrongCount}")


"""function to display guessed letters
    use global vaiable rightCount 
    to the number of letters correctly guessed.
    store guused leter in place
    store "_" for letters still hidden"""


def displayGuessedLetters(word, guessedLetters):

    global rightCount
    lettersGuessedDisplayList = []
    for letter in word:
        if letter.upper() in guessedLetters:
            lettersGuessedDisplayList.append(letter.upper())
            rightCount += 1
        else:
            lettersGuessedDisplayList.append("_")
    return " ".join(lettersGuessedDisplayList)


# Main Program
while True:
    # exit loop if player answered "Y"
    if playAgain.lower() != "y":
        print("Thank You! for Playing")
        break

    # set/reset the game
    lettersGuessedList = []
    lettersGuessedDisplay = ""
    wrongCount = 0
    rightCount = 0
    wordSelected = choice(wordList)
    letterCount = len(wordSelected)

    # Welcome Screen
    print("Welcome to Hangman!")
    # replace all letter with underscores
    lettersGuessedDisplay = displayGuessedLetters(
        wordSelected, "_ " * letterCount)
    print("YOU HAVE 10 SECONDS TO ANSWER. HURRY!!!")

    while True:
        print(f"{drawingHang[wrongCount]}")
        print(f"the word has {letterCount} letters: {lettersGuessedDisplay}")

        # Loss Condition
        if wrongCount == maxWrongGuess:
            print(
                f"Sorry, you ran out of attempts. The word was: {wordSelected}")
            break
        # Win Condition
        if rightCount == letterCount:
            print(f"Congratulations! You guessed the word: {wordSelected}")
            break
        # get user input with timeout
        inputTimer = Timer(10, timeout)
        inputTimer.start()
        guessLetter = getUserInput()
        inputTimer.cancel()

        # process input
        if guessLetter.isnumeric():
            # handle numeric input
            print("Invalid input. Enter a letter ")
            wrongCount += 1
            continue
        elif guessLetter.isalpha() and len(guessLetter) == 1:
            # add each correct answer to a list then call the display function to print
            if guessLetter.upper() in wordSelected:
                lettersGuessedList.append(guessLetter.upper())
                lettersGuessedDisplay = ""
                rightCount = 0
                lettersGuessedDisplay = displayGuessedLetters(
                    wordSelected, lettersGuessedList)
            else:
                wrongCount += 1
                print("Wrong Answer! Try Again!")
            print(
                f"the word has {letterCount} letters: {lettersGuessedDisplay}")
#            print(f"right count = {rightCount}")
#            print(f"wrong count = {wrongCount}")
#            print(f"letter Count = {letterCount}")
        else:
            print("Invalid input. Enter a single letter ")
            wrongCount += 1
            continue

    playAgain = input("Play Again? (press Y for yes)")

