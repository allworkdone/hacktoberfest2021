from turtle import *    # use the turtle library
from sys import *

wn = Screen()
mateo = Turtle()
mateo.setheading(90)

for repeats in range(20):
    mateo.color("red")
    mateo.forward(10)
    mateo.left(18)

    for sides in range(3):
        mateo.pencolor("blue")
        mateo.forward(50)
        mateo.right(120)
