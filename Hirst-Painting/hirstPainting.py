import random
import turtle


#below is the code to detect colours from colorgram library
# import colorgram
#
# colors = colorgram.extract('rgb.jpg' ,6)
#
# rgb_colours =[]
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colours.append(new_color)
#
# print(rgb_colours)
#


#Actual code to draw the hirst painting:
from turtle import *
turtle.colormode(255)
object = Turtle()
object.hideturtle()
object.speed(0)
object.penup()
color_list =[(85, 253, 150), (167, 1, 120), (250, 248, 226), (225, 252, 235), (15, 210, 74), (25, 14, 185)]
object.setheading(225)
object.forward(300)
object.setheading(0)
number_of_dots = 100



for dot_count in range(1,number_of_dots+1):
    object.dot(20 ,random.choice(color_list))
    object.forward(50)

    if dot_count % 10 == 0:
        object.setheading(90)
        object.forward(50)
        object.setheading(180)
        object.forward(500)
        object.setheading(0)













Screen().exitonclick()
