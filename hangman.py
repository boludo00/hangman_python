# Simple console-based interactive hangman. To run: python hangman.py 

import random

HANGMANPICS = [''' 
  
  +---+
  |   |
      |
      |
      |
      |
 =======''','''
  +---+
  |   |
  O   |
      |
      |
      |
 =======''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
 =======''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
 =======''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
 =======''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
 =======''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 =======''']

# start with an empty list and append a words from a dictionary
words = []

# append contentsof a dictionary text file to an empty list
myfile = open("dictionary.txt", "r")
for line in myfile.read().splitlines():
  words.append(line)
#print(thislist)

# word bank, and split into list
#words = 'Unkemptly quadrangled knickerbocker incisively protanomaly nonadherent inattentively resemblance carney demphasis nonministerial couperin untedded hispanism. Bluebeard sylva invigilating emulsifier oversolicitous poisoner cosmically alwin kirsten exon moralistic judith fecula mattress Flabellum mithridatising test estival viceless fumage tehillim lounging detachedly bravissimo slumbrous bemuse attainer idolatrously. Suberin brooklet vittorio clemently quipster peart cryptoanalyst tinker amatorially boyishness hypsographic mill unhomogenized undeliverable telophase copaline nictitant outlive econ ephesus hutch embruting corporalship rarebit laborism palatal intemerate'.split()

# function to print the blanks
def generateBlanks(word):
  blanks =[]
  for c in word:
    blanks.append("_ ")
  return blanks
    #print("_", end=" ")
  #print("\n")

# function returns a list of indeces where the letter is in the word
def isInWord(letter, word):
  index = 0
  indList = []
  while index < len(word):
    index = word.find(letter, index)
    if index == -1:
      break
    else:
      indList.append(index)
    index += 1
  return indList

# function to print individual hangmen 
def showHangman(guesses):
  if guesses == 0:
    print(HANGMANPICS[0])
  elif guesses == 1:
    print(HANGMANPICS[1])
  elif guesses == 2:
    print(HANGMANPICS[2])
  elif guesses == 3:
    print(HANGMANPICS[3])
  elif guesses == 4:
    print(HANGMANPICS[4])
  elif guesses == 5:
    print(HANGMANPICS[5])
  elif guesses == 6:
    print(HANGMANPICS[6])
  


#============================================================================
# Start of program
#============================================================================

#initiate guesses to 0
guesses = 0

# underscore val
underscore = '_'

# counter
counter = 0

#for list of letters not in word
alreadyGuessed = []

# randomly select a word form the list
goalWord = random.choice(words)
#print(goalWord)

# represent blanks as a list
blanks = generateBlanks(goalWord)

# play the game as while user hasnt lost
while guesses < 7:
  if guesses == 6:
    print("Oh no! You lost, sorry.")
    print("The word was " + "'" + goalWord + "'")
    showHangman(guesses)
    break
  showHangman(guesses)
  print(''.join([str(blank) for blank in blanks]))
  #print(*blanks, sep = " ")
  print("Guess a letter...")
  
  # take user input
  guess = input()

  # check if user entered a letter
  while not guess.isalpha():
    print("Please only guess the letters 'a' - 'z'")
    guess = input()
    showHangman(guesses)


  # error handling for user not entering a single letter
  while len(guess) > 1:
    print("Please only guess a single letter. Try again.")
    guess = input()
    showHangman(guesses)

  # allow user to guess again if they guessed the same letter twice
  if guess in alreadyGuessed:
    print("You've already guessed " + guess + ", guess again.")
    continue

  # list of indeced where letter is
  indeces = isInWord(guess, goalWord)
  #print(indeces)

  # if indeces is empty, letter not in word
  if len(indeces) == 0:
    print("Letter " + str(guess) + " not present")
    # append guessed letter to list of already guessed
    alreadyGuessed.append(guess)
    guesses += 1
  else: # letter is in word
    print("Yep! The phrase contains a(n) " + "'" + guess + "'")
    # update blanks
    for i in indeces:
      blanks[i] = guess
      alreadyGuessed.append(guess)
      counter += 1 # keep track of counter, increment when guess correctly.


  if counter == len(goalWord): # player has won the game
    print("Congratulations! The word was " + goalWord +". You win hangman.")
    break

  # display guessed letters only when user has already guessed 
  if guesses > 0:
    print("You've already guessed the following: " + " ,".join([str(thing) for thing in alreadyGuessed]))
    
