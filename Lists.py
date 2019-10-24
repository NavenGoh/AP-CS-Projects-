favFoods = ["Miso Soup", "Rice", "Curry"]
# These start counting from 0, then 1, then 2, etc
print(favFoods[0])
print(favFoods[2])
# print(favFoods[3]) = error, b/c the index starts counting from 0, not 1. 
print(favFoods)
# Adds to the end of the list
favFoods.append("Yogurt")
print(favFoods)
print(favFoods[3]) # Now it works b/c you added yogurt to the list
print("My 4th favorite food is " + favFoods[3])
# Insert - Adds an index in a list
favFoods.insert(1, "Chicken")
print(favFoods)
# Removes an item from the list
favFoods.remove("Chicken")
print(favFoods)
# Remove by index (which refers to the position it is in the list)
favFoods.pop(0)
print(favFoods)

favFoods.insert(0, "pizza")
# loop through a list (IMPORTANT)
for food in favFoods:
	print(food)

numList = [1, 2, 3, 4, 5, 6, 7, 8]

# loop through the list, and add all the numbers together. Then print sum.
sum = 0 #This is outside the for loop b/c we want to add everything AT THE END
for num in numList:
	sum = sum + num

print(sum)
# function to get the length of a list
print(len(numList))

# make a list for favorite movies
# prompt for a favorite movie

myFood = input("What is your favorite food?")
favFoods.append(myFood)
print(favFoods)
myMovie = ["Back to the Future", "Dumb and Dumber", "Barnyard"]
addMovie = input("What is your favorite movie?")
myMovie.append(addMovie)
print(myMovie)

# List methods and functions
# append - adds item to the end of a list
# insert - adds an item toa specified index
# remove - removes a specified item from a list
# pop - removes item from a specified index
# len - returns the length of a list
print(favFoods[len(favFoods) - 1])
