# imports
import os
import random

# print instructions
os.system("clear")
print ("This is a game of hangman. Player will have to guess the word. Each turn will consist of the player guessing one letter.\n\n"
	"If the letter is in the word, all instances of the letter in the word will be revealed.\n\n"
	"If the letter is not in the word, then the player will lose one life. If the player loses 10 lives, then the game will be over.\n\n"
	"Press any key to begin the game!")
input()
os.system("clear")

# global variables
roundNum = 1
GAME_OVER = False
GUESSES = list()

# player class
class Player(object):
	"""Class defining a player"""
	def __init__(self):
		self.lives = 10
	
	def lifeLost(self):
		print ("Incorrect guess, you lose 1 life.")
		self.lives -= 1
		if self.lives == 0:
			gameOver()

# instantiate a player object
p1 = Player()

# populate the word list and choose a random word
word_list = list(line.strip() for line in open('words_alpha.txt'))
WORD = ""
while len(WORD) < 6:
	WORD = random.choice(word_list)
WORD_CHARS = list(WORD)

# create a list to show progress in guessing
PRINT_CHARS = list()
for i in WORD_CHARS:
	PRINT_CHARS.append("_")

# necessary functions
def wordGuessed(word):
	os.system("clear")
	print ("WINNER! The word was : ", word)
	return True

def gameOver():
	os.system("clear")
	print ("GAME OVER! The word was : ", WORD)
	return True

def isPresent(guess):
	if guess in WORD:
		pos = findLetter(guess)
		revealLetter(pos, guess)
	else:
		p1.lifeLost()

def findLetter(guess):
	pos = list()
	index = 0
	while index < len(WORD_CHARS):
		if guess == WORD_CHARS[index]:
			pos.append(index)
		index += 1
	return pos

def revealLetter(pos, guess):
	for i in pos:
		PRINT_CHARS[i] = guess

def printChars():
	print(' '.join(PRINT_CHARS))

def checkWord():
	if '_' not in PRINT_CHARS:
		return True

def updateGuesses(guess):
	if not checkGuess(guess):
		GUESSES.append(guess)
		return False
	else:
		return True

def checkGuess(guess):
	if guess in GUESSES:
		return True

# main game loop
while not GAME_OVER:
	print("ROUND ", roundNum, "\n")
	printChars()
	print ("\nCurrent lives = ", p1.lives)
	letter = input("Enter your guess OR enter 1 to see your guesses: ")
	print()
	if letter != '1':
		b = updateGuesses(letter)
		if not b:
			isPresent(letter)
			b = checkWord()
			if b:
				GAME_OVER = wordGuessed(WORD)
			if p1.lives == 0:
				GAME_OVER = gameOver()
		else:
			print ("Already guessed, please guess again.\n")
	else:
		print(', '.join(GUESSES))
		print()
	print()
	roundNum += 1