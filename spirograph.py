import turtle as t
from turtle import Screen
import random

screen = Screen()
screen.bgcolor("yellow")
tim = t.Turtle()
tim.speed('fastest')
tim.shape("turtle")
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap,radius):
    for i in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(radius)
        # current_heading=tim.heading()
        # tim.setheading(current_heading+10)
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(5,100)
draw_spirograph(5,150)
screen.exitonclick()
