import turtle
def draw():
	window = turtle.Screen()
	window.bgcolor("red")

	nate = turtle.Turtle()
	me = turtle.Turtle()

	for i in range(4):
		nate.forward(100)
		nate.right(90)

	me.circle(100)

	window.exitonclick()


draw()