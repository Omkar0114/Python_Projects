from turtle import *
object = Turtle()
myScreen = Screen()

def move_fd():
    object.forward(20)


def move_back():
    object.backward(20)

def move_right():
    new_heading = object.heading() + 10
    object.setheading(new_heading)

def move_left():
    new_heading = object.heading() -10
    object.setheading(new_heading)

def draw_circle():
    object.circle(90)

def clear():
    object.clear()
    object.penup()
    object.home()
    object.pendown()


myScreen.listen()
myScreen.onkey(move_fd , "Up")
myScreen.onkey(move_back , "Down")
myScreen.onkey(move_left , "Left")
myScreen.onkey(move_right , "Right")
myScreen.onkey(draw_circle , "s")
myScreen.onkey(clear , "c")
myScreen.exitonclick()
