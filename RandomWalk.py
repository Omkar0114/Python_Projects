import turtle as t;
import random

object = t.Turtle()
t.colormode(255)
object.pensize(10)
object.speed(10)
def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r ,g ,b)

directions = [0,90,180,270]

for _ in range(200):
    object.color(randomcolor())
    object.forward(35)
    object.setheading(random.choice(directions))














myscreen = Screen()
Screen().exitonclick()
