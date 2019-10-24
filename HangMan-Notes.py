
myWord = "Hello"
choice = input("Type a word: ")
if choice == myWord:
 	print("It's a match")
else:
 	print("Not a match")


# How to check if a letter is in a word

letter = input("Enter a letter: ")

if letter in myWord:
	print("Letter matches")
else: 
	print("Letter is not in word")

count = 0
# myList = list(myWord)
for letter2 in myWord:
	if letter2 == letter:
		print(count)
	count += 1
# string into a list: Makes each letter into an index in a list

myString = "Arizona"
mystery = list(myString)
print(mystery)
guessList = []
# How to make a list with _ for characters instead of the letters

for letter in mystery:
	guessList.append("_")

print(guessList)

# How to replace a specific index in a list

guessList[3] = "z"

print(guessList)

secretWord = "Christmas"
secret = list(secretWord)
misses = 0
hangman = ["first pic", "second pic"]

guess = input("Guess a letter: ")
if guess in secret:
	print("Letter in word")
	count = 0
	for letter in mystery: 
		if letter == guess:
			guessList[count] = guess 
else:
	misses = misses + 1

print("Misses: " + str(misses))
print(hangman[misses])