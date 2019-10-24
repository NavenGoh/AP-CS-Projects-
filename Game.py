from turtle import*

scoreT = Turtle()
screen = scoreT.getscreen()
scoreT.penup()
scoreT.goto(screen.window_width() / 2 - 200, screen.window_height()/2 - 50)
scoreT.hideturtle()
score = 0 

def updateScore():
	scoreT.clear()
	scoreT.write("Score: " + str(score), False, "left", font = ("Arial", 20, "normal"))

updateScore()

screen.mainloop()