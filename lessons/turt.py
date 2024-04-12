from turtle import Turtle, colormode, done

side=400

leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
colormode(255)
leo.color(99, 204, 250)
leo.penup()
leo.goto(-side/2, -100)
leo.pendown()

leo.begin_fill()
for i in range(3):
    leo.forward(side)
    leo.left(120)
leo.end_fill()

bob: Turtle = Turtle()
bob.speed(50)
bob.hideturtle()
bob.pencolor("black")
bob.penup()
bob.goto(-side/2, -100)
bob.pendown()

for i in range(90):
    bob.forward(side)
    bob.left(122)
    side*=0.98
    


done()