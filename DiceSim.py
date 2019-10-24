# Naven Goh
# Period 1
# October 2, 2019

#import random 
#TotalRoll = int(input("How many times would you like to roll the di?"))
#mysteryNum = random.randint(1, 6)
#def diceroll():
#while rolls <= int(TotalRoll):
	#face1 = 0
	#face2 = 0
	#face3 = 0
	#face4 = 0
	#face5 = 0
	#face6 = 0 
	#if rolls > int(TotalRoll):
		#break

	#if mysteryNum == 1:
 		#face1 += 1
	#elif mysteryNum == 2:
	#	face2 += 1
	#elif mysteryNum == 3:
	#	face3 += 1
	#elif mysteryNum == 4:
	#	face4 += 1
	#elif mysteryNum == 5:
	#	face5 += 1
	#else:
	#	face6 += 1
    
#print ("1:" + str(face1))
#print ("2:" + str(face2))
#print ("3:" + str(face3))
#print ("4:" + str(face4))
#print ("5:" + str(face5))
#print ("6:" + str(face6))

import random
TotalRoll = int(input("How many times would you like to roll the di?"))
x = random.random()

rolls = 0
def diceroll():
	r = random.randint(1,6) 
	if r == 1.0:
		r = 1
	elif r == 2.0:
		r = 2
	elif r == 3.0:
		r = 3
	elif r == 4.0:
		r = 4
	elif r == 5.0:
		r = 5
	else:
		r = 6
     
	return r
     
for x in range(TotalRoll):
	rolls += 1
	diceroll()
	D1 = diceroll()
	print(str(rolls) + " Result: " + str(D1))