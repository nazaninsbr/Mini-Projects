import turtle
def drawSquare():
	window = turtle.Screen()
	window.bgcolor("red")

	nate = turtle.Turtle()
	nate.shape("turtle")
	nate.color("white")


	for i in range(4):
		nate.forward(100)
		nate.right(90)

	window.exitonclick()


drawSquare()