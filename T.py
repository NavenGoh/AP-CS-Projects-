from turtle import *

T = Turtle()
screen = T.getscreen()
T.forward(200)

def printName():
	name = screen.textinput("name", "What is your name?")
	T.write(name, move=True, align="left", font=("Arial", 40, "normal"))
	screen.listen()

def goForward():
	T.forward(10)

def turnRight():
	myTurtle.right(90)

screen.onkey(turnRight, "Right")
screen.onkey(goForward, "Up")
screen.onkey(printName, "p")

screen.listen()
screen.mainloop()
