import turtle
def draw():
	window = turtle.Screen()
	window.bgcolor("red")

	nate = turtle.Turtle()
	nate.shape("turtle")
	nate.color("white")

	for x in range(9):
		for i in range(4):
			nate.forward(100)
			nate.right(90)
		nate.right(160)

	window.exitonclick()


draw()