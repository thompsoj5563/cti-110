#CTI 110
#Jessica Thompson
#March 22, 2018
#P4Lab1 - Nested Loops


import turtle
wn = turtle.Screen()
t = turtle.Turtle()


for x in range(6):
    for i in range(3):
        t.forward(100)
        t.right(120)
    t.forward(100)
    t.left(60)

turtle.done()
