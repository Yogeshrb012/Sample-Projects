import random
import turtle

liner = turtle.Turtle()


liner.speed(2500)

colours = ["red", "yellow", "green", "blue", "orange", "brown", "black", "pink"]
for i in range(360):
    liner.forward(100)
    liner.right(30)
    liner.color(random.choice(colours))
    liner.forward(20)
    liner.left(60)
    liner.forward(50)
    liner.right(30)

    liner.penup()
    liner.setposition(0, 0)
    liner.pendown()

    liner.right(1)

turtle.done()
