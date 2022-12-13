import random
from colorama import Fore, Style 

def printInstructions():
    print("Enter a 5 letter word: ")
def getRandomWord():
    words = open("/Users/edisonlin/CPSC 230/CPSC230 /ELin_Assignment6/words.txt")
    wordList= words.readlines()
    word = random.choice(wordList)
    return word
def readInput(a):
    with open('/Users/edisonlin/CPSC 230/CPSC230 /ELin_Assignment6/words.txt') as f:
        wordList = f.readlines()
        wordList = [x.strip() for x in wordList]
    while (len(a) != 5) or (a not in wordList):
        print("You need to guess an actual 5 letter word.")
        a = input("Enter a guess: ") # Asks user for guess
    else:
        return True
def getGuess():
    guess = " "
    guess = input("Enter a guess: ")
    return guess
def colorCheck1(a, b):
  c = 0
  first_Letter = a[0]
  if first_Letter in b[0]:  # correct
    c += 2
    return c
  elif first_Letter in (b[1 : 4]):  # almost correct
    c += 1
    return c
  elif first_Letter not in (b[0 : 4]):  # incorrect
    return c
def colorCheck2(a, b):
  c = 0
  second_Letter = a[1]
  if second_Letter in b[1]:  # correct
    c += 2
    return c
  elif second_Letter in b[2 : 4]:  # almost correct
    c += 1
    return c
  elif second_Letter in b[0]:  # almost correct
    c += 1
    return c
  elif second_Letter not in (b[0 : 4]):  # incorrect
    return c
def colorCheck3(a, b):
  c = 0
  third_Letter = a[2]
  if third_Letter in b[2]:  # correct
    c += 2
    return c
  elif third_Letter in b[3 : 4]:  # almost correct
    c += 1
    return c
  elif third_Letter in b[0 : 1]:  # almost correct
    c += 1
    return c
  elif third_Letter not in (b[0 : 4]):  # incorrect
    return c
def colorCheck4(a, b):
  c = 0
  fourth_Letter = a[3]
  if fourth_Letter in b[3]:  # correct
    c += 2
    return c
  elif fourth_Letter in b[0 : 2]:  # almost correct
    c += 1
    return c
  elif fourth_Letter in b[4]:  # almost correct
    c += 1
    return c
  elif fourth_Letter not in (b[0 : 4]):  # incorrect
    return c
def colorCheck5(a, b):
  c = 0
  fifth_Letter = a[4]
  if fifth_Letter in b[4]:  # correct
    c += 2
    return c
  elif fifth_Letter in b[0 : 3]:  # almost correct
    c += 1
    return c
  elif fifth_Letter not in (b[0 : 4]):  # incorrect
    return c
def colorChange(a):
    color = ()
    for i in range(a):
        if a == 2:
            color.append(Fore.GREEN + a[i] + ' ', end='')
            return color
        elif a == 1:
            color.append(Fore.YELLOW + a[i] + ' ', end='')
            return color
        elif a == 0:
            color.append(Fore.WHITE + a[i] + ' ', end='')
            return color

printInstructions()
word = getRandomWord()
word_split = word.splitlines
attempt = 0
guess = getGuess()
bruh = readInput(guess)
while bruh == True and attempt < 6:
    a = colorCheck1(guess, word)
    print(colorChange(a, guess[0]))
    b = colorCheck1(guess, word)
    print(colorChange(b, guess[1]))
    c = colorCheck1(guess, word)
    print(colorChange(c, guess[2]))
    d = colorCheck1(guess, word)
    print(colorChange(d, guess[3]))
    e = colorCheck1(guess, word)
    print(colorChange(e, guess[4]))
    if attempt < 6:
        attempt += 1
    elif attempt > 6:
        print("You lost! ")
