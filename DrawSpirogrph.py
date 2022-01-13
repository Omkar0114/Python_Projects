import random
import turtle
from turtle import *


object = Turtle()
turtle.colormode(255)


def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randomColor = (r,g,b)
    return randomColor

object.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        object.color((randomcolor()))
        object.circle(100)
        object.left(5)

draw_spirograph(5)












Screen().exitonclick()
