# This is a check and review to make sure nothing was lost over break

# Naven
# Period 1

# Variable declaration and assignment
# Example
myVar = "hello"
# You try, declare two variables, 1 string and 1 number, and assign values
TestOne = 3
TestA = "What?"

# While loop
# Example
x = 10 
while x > 0:
	print(x)
	x = x - 1

# You try, print your name 100 times
n = 100
while n > 0:
	print("Naven Goh")
	# print(n) - This will list off the numbers when you uncomment this out
	n = n - 1
	# do not do this
	# print("Naven" * 100)

# String Concatenation
# Example
name = "Naven"
print("Hello" + name)
# Check - make a variable with your favorite movie
# print "my favorite movie is... variable"
movie = "Back To The Future"
print("My favorite movie is " + movie)

# input
# Example 
myName = input("What is your name? ")
print("Your name is " + myName)
# prompt for favorite song and print "Your favorite song is..."

mySong = input("What is your favorite song?")
print("Your favorite song is " + mySong)\

# casting; Changing the type if a variable
myNumber = 64
print("My number is " + str(myNumber))
num1 = input("Enter a number: ")
num1 =int(num1) + 10
print("num1 + 10 is " + str(num1))

# Ask for two numbers, add them and print the answer
Add1 = input("Enter a number: ")
Add2 = input("enter another number: ")
Add3 = int(Add1) + int(Add2)
print("The first number plus the second number is " + str(Add3))

Yerr = input("Type a number: ")
if int(Yerr) > 100:
	print("Your number is more than 100")
elif int(Yerr) == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")

# Ask if today is your bithday, if it is, then print Happy birthday

bDay = input("Is today your birthday?")
if bDay == "yes":
	print("Happy birthday!")
elif bDay == "no":
	print("Oh well.") 
else:
	Print("Please say yes or no.")