print("Welcome to To Do List")
# Make a variable to hold your list, can be empty
ToDo = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Choose: ")

	if choice == "q":
		break
		print("OmegaLUL irresponsible")
	elif choice == "a": # adding an item to the list
		A = input("Add: " )
		ToDo.append(A)
	elif choice == "r": # removing an item from the list
		R = input("Remove: ")
		ToDo.remove(R)
	elif choice == "p": # print the list
		x = 0
		N = 1
		K = 0
		while x < int(len(ToDo)):
			x = x + 1
			print("Task " + str(N) + ": " + ToDo[int(K)])
			N = N + 1
			K = K + 1
	else:
		print("Please enter valid entry")



# print("Welcome to To Do List")
# Make a variable to hold your list, can be empty
#ToDo = []
#while True:
	#print("Enter a to add an item")
	#print("Enter r to remove an item")
	#print("Enter p to print the list")
	#print("Enter q to quit")
	#choice = input("Choose: ")

	#if choice == "q":
	#	break
	#	print("OmegaLUL irresponsible")
	#elif choice == "a": # adding an item to the list
	#	A = input("Add: " )
	#	ToDo.append(A)
	#elif choice == "r": # removing an item from the list
	#	R = input("Remove: ")
	#	ToDo.remove(R)
	#elif choice == "p": # print the list
	#	print(str(ToDo))
	#else:
	#	print("Please enter valid entry")
