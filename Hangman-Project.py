import random
import time
import sys

myWordList = ["mathematics", "computers", "rhythm", "games", "sleep"]

guessList = []

myWord = random.choice(myWordList)
MissCount = 0 
count = 0
GuessNumber = input("How many lives would you like to have? (Each missed letter loses a life) Pick between 1 and 9 ")




for letter in myWord:
	guessList.append("_")

if int(GuessNumber) >= 10:
	sys.exit("Can you read?")
elif int(GuessNumber) == 0:
	sys.exit("I guess you lost then")
while int(MissCount) <= int(GuessNumber):

	choice = input("Enter a letter: ")

	if choice in myWord:
		print("Match!")
		for letter in myWord: 
			if letter == choice:
				guessList[count] = choice
			count = count + 1
		print(guessList)
	else:
		print("Not a match")
		MissCount = MissCount + 1
		Attempts = int(GuessNumber) - MissCount
		print("You have " + str(Attempts) + " remaining attempts left." )
		print(guessList)
	if MissCount == int(GuessNumber):
		print("You lose. Game Over.")
		break
# myList = list(myWord)
	#for letter in myWord:
	#	if choice == letter:
	#		count += 1
	#		print(count)
	#		print("Success")	
	#	else:
	#		MissCount = MissCount + 1
	#		Attempts = 7 - MissCount
	#		print("Incorrect, try again. ")
# string into a list: Makes each letter into an index in a list

	#myString = str(myWord)
	#mystery = list(myString)

	#guessList = []
# How to make a list with _ for characters instead of the letters

#	for letter in mystery:
	#	guessList.append("_")

	#print(guessList)

# How to replace a specific index in a list




	#print("Game Over")

	#if choice == letter:
	#	print("Good job, keep going!")
	#else:
	#	print("You have " + str(Attempts) + " remaining attempts left." )
	#if guess in secret:
	#print("Letter in word")
	#count = 0
	#for letter in mystery: 
	#	if letter == guess:
	#		guessList[count] = guess 	