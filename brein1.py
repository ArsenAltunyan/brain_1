import turtle

brain = turtle.Turtle()
brain.speed(100)

def square_parameter (a):
    for i in range(4):
        brain.forward(a)
        brain.left(90)

brain = turtle.Turtle()
brain.speed(100)

dlina=40
for i in range(16):
    square_parameter(dlina)
    dlina=dlina+18