# Naven Goh
# Rock Paper Scissors Game
# _______________________________________________________________________________________
# break into pieces
# Welcome page, with name entry
# Score screen with Computer, player (name), ties
# Options for game: r, p, s, q
# Game will loop until q is entered
# Each loop it will get a random choice from the computer
# A choice from the player, compare the two, and update the score
# When the game is over (q is entered) the final score is displayed

# WELCOME PAGE
# Prompt for the player name
# Welcome message

#_______________________________________________________________________________________
# imports
import random
# variables
playerScore = 0
computerScore = 0
ties = 0
# Make a list
cChoices= ["r", "p", "s"]
# random lets you pick out of a list
print("Welcome to Rock Paper Scissors")
Name = input ("Enter your name")
# MainLoop
while True:
	#print score
	print("Score: ")
	print("Computer: " + str(computerScore))
	print(Name + " " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' for Quit: ")
	computerChoice = random.choice(cChoices)
	if choice == "q":
		print("Score: ")
		print("Computer: " + str(computerScore))
		print(Name + " " + str(playerScore))
		print("Ties: " + str(ties))
		print("Thanks for playing!")
		break

	if choice == "r":
		print(Name +" Picked Rock")
		if computerChoice == "r": # A tie occurs
			print("Computer picked Rock")
			print("This is a tie")	
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock")	
			computerScore += 1
		else: # s is the only choice left
			print("Computer picked Scissors")
			print("Rock beats Scissors")	
			playerScore += 1 
	elif choice == "p":
		print(Name +" Picked Paper")
		if computerChoice == "r": 
			print("Computer picked Rock")
			print("Paper beats Rock")	
			playerScore += 1 		
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")	
			ties = ties + 1
		else: # s is the only choice left
			print("Computer picked Scissors")
			print("Scissors beats Paper")	
			computerScore += 1
	elif choice == "s":
		print(Name +" Picked Scissors")
		if computerChoice == "r": 
			print("Computer picked Rock")
			print("Rock beats Scissors")
			computerScore += 1	
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Scissors beats paper")	
			playerScore += 1
		else: # s is the only choice left
			print("Computer picked Scissors")
			print("This is a tie")	
			ties = ties + 1

	else:
		print("Invalid Entry, please try again")



