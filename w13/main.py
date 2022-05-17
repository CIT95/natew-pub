import turtle
import random
from colors import color_list

screen = turtle.Screen()
screen.setup(width=900, height=900)

turtle.colormode(255)
brush = turtle.Turtle()
brush.penup()
brush.setposition(-350, -350)
brush.hideturtle()
brush.speed(10)

screen.textinput(title="Match the Turtle", prompt="Connect all the dots \
that match the color of the turtle.")


def painting_creation(total_dots):
    for dots in range(1, total_dots + 1):
        paint()
        if dots % 10 == 0:
            brush.setheading(90)
            brush.forward(70)
            brush.setheading(180)
            brush.forward(700)
            brush.setheading(0)


def paint():
    brush.dot(20, random.choice(color_list))
    brush.forward(70)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_counter():
    tim.left(10)


def move_clock():
    tim.right(10)


number_dots = 100
painting_creation(number_dots)

tim = turtle.Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.color(random.choice(color_list))
tim.penup()
tim.setposition(x=-380, y=0)
tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter)
screen.onkey(key="d", fun=move_clock)


screen.exitonclick()
