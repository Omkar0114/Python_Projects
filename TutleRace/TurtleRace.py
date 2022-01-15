import random
from turtle import *

screen = Screen()
is_race_on = False
screen.setup(width=500 , height=400)
user_bet = screen.textinput("Turtle Race " , "Which colour will win ? Enter a color:")
colors = ["red" ,"orange" ,"yellow" ,"blue" ,"green" ,"purple"]
all_turtles =[]

y_positions = [-70,-40 ,-10 ,30,70,100]
for turtle_index in range (0,6):
    newTurtle= Turtle(shape="turtle")
    newTurtle.color(colors[turtle_index])
    newTurtle.penup()
    newTurtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(newTurtle)




if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won ! {winning_colour} turtle won the race")
            else:
                print(f"You've lost ! {winning_colour} turtle won the race")






        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()
