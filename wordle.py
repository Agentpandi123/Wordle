import random
from colorama import Fore, Style 

def printInstructions():
    print("Enter a 5 letter word: ")

def getRandomWord():
    words = open("/Users/edisonlin/CPSC 230/CPSC230 /ELin_Assignment6/words.txt")
    wordList= words.readlines()
    word = random.choice(wordList)
    return word

def readInput(guess):
    words = open("/Users/edisonlin/CPSC 230/CPSC230 /ELin_Assignment6/words.txt")
    wordList= words.readlines()
    if guess not in wordList:
        return "False"
    if guess in wordList:
        return "True"

def getGuess():
    guess = " "
    guess = input("Enter a guess: ")
    while len(guess) != 5:
        guess = input("Enter a guess: ") # Asks user for guess
        return guess # Returns guess value once guess is valid

def colorChange(gues, word):
    color = ()
    for i, item in enumerate(guess):
        if item == word[i]:
            color.append(f'{Fore.GREEN}{item}{Style.RESET_ALL}')
            return color
        elif item in word:
            color.append(f'{Fore.YELLOW}{item}{Style.RESET_ALL}')
            return color
        else:
             color.append(item)
             return color


printInstructions()
word = getRandomWord()
word_split = word.splitlines
attempt = 0
guess = getGuess()
bruh = readInput(guess)
if bruh == "False":
    print("You need to guess an actual 5 letter word.")
    guess = getGuess()
while bruh == "True" and attempt < 6:
    print(guess)
    color = colorChange(guess, word)
    print(color)
    if attempt < 6:
        attempt += 1
    elif attempt > 6:
        print("You lost! ")
