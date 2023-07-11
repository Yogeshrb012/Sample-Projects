import turtle
from turtle import Turtle, Screen
import random
# tim=Turtle()
screen=Screen()

is_game_over=False
colors=["red","black","brown","yellow","blue","green"]
y_cordinates=[-175, -150, -125, -100, -75, -50, -25]
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="make your bet!", prompt="which turtle will win?")
all_turtle=[]
#print(user_guess)
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cordinates[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_game_over=True

while is_game_over:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_game_over= False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"you've won! {winning_color} turtle won the race")
            else:
                print(f"you've lost! {winning_color} turtle won the race")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
# def intl_pos():
#     tim.penup()
#
#     tim.pendown()
#     tom.penup()
#     tom.goto(x=-230, y=-150)
#     tom.pendown()
#
# intl_pos()

# def forward():
#     arrow.forward(20)
#
# def back():
#     arrow.back(20)
#
# def clck():
#     arrow.right(-90)
#     arrow.forward(20)
#
# def antclck():
#     arrow.right(90)
#     arrow.forward(20)
#
# def clear():
#     arrow.clear()
#     arrow.penup()
#     arrow.home()
#     arrow.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=back)
# screen.onkey(key="a", fun=clck)
# screen.onkey(key="d", fun=antclck)
# screen.onkey(key="c",fun=clear)





























screen.exitonclick()
