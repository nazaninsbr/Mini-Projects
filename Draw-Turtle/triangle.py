import turtle
def draw():
	window = turtle.Screen()
	window.bgcolor("red")

	nate = turtle.Turtle()
	nate.shape("turtle")
	nate.color("white")

	for i in range(3):
		nate.forward(100)
		nate.left(120)

	window.exitonclick()


draw()