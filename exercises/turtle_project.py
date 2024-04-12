"""This is a turtle program that creates a little landscape scene. I use randomness to vary the ground, clouds and height of the mountains to add variety each time the program is run."""
 
__author__ = "730704805"
 
from turtle import Turtle, colormode, done 
from random import randint
 
 
def main() -> None:
    """The entrypoint of my scene."""
    turt: Turtle = Turtle()
    turt.hideturtle()

    turt.speed(0)
    colormode(255)
    turt.screen.bgcolor(86, 160, 211)
    turt.screen.screensize(1000, 1000)

    mountains(turt, -100, -250)
    sun(turt, 300, 250)
    for i in range(3):
        clouds(turt, -300 + i * 300, 170, 3)
    ground(turt, -200)

    done()


def clouds(t: Turtle, x: float, y: float, num_of_cloud: int) -> None:
    """Uses recursion to draw clouds by checking how many clouds have been drawn and only returning to main when num_of_cloud is 0."""
    t.color("white")
    if num_of_cloud == 0:
        return
    else:
        size = randint(-12, 12)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        octagon(t, 50 + size)
        t.end_fill()
        
        clouds(t, x + 65, y + randint(-10, 10), num_of_cloud - 1)


def ground(t: Turtle, height: float) -> None:
    """Draws a random landscape and then fills in below."""
    t.setheading(0.0)
    t.color(16, 92, 5)
    t.penup()
    t.goto(-500, height)
    t.pendown()

    t.begin_fill()
    for i in range(5):
        t.forward(200)
        t.left(randint(-20, 20))
    t.setheading(270)
    t.forward(1000)
    t.setheading(180)
    t.forward(1000)
    t.end_fill()


def mountains(t: Turtle, x: float, y: float) -> None:
    """Uses basic triangles and variety in color in the fill and pen tool to add some shading."""
    for i in range(3):
        t.penup()
        t.goto(x + i * 70, y)
        t.pendown()
        t.begin_fill()
        t.color(245, 243, 240)
        tri(t, 200 + randint(0, 100))
        t.color(148, 147, 145)
        t.end_fill()


def sun(t: Turtle, x: float, y: float) -> None:
    """Messed around with turning and movement to try and create something resembling a sun."""
    t.setheading(0.0)
    t.color(255, 235, 87)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(100):
        t.forward(100)
        t.left(185)
        t.forward(100)
    

def octagon(t: Turtle, len: int) -> None:
    """Helper function to make an octagon."""
    for i in range(8):
        t.forward(len)
        t.left(45)


def tri(t: Turtle, height: float) -> None:
    """Helper function to make a triangle."""
    t.setheading(0.0)
    t.left(120)
    t.forward(height)
    t.left(120)
    t.forward(height)
 

if __name__ == "__main__":
    main()