import turtle

t = turtle.Turtle()
s = turtle.Screen()
r=50
number = 0

t.speed(50)
t.circle(50)
t.forward(200)
t.right(180)
t.forward(130)
t.right(90)
t.forward(-90)
t.right(50)
t.forward(142)
t.right(40.5)
t.forward(20)
t.right(89)
t.forward(100)
t.right(90)
t.forward(183)
t.right(90)
t.forward(100)
t.right(180)
t.forward(100)


while number <4:
    t.forward(100)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.right(90)
    number += 1

t.left(97)
t.forward(150)
t.right(180)
t.right(97)
t.forward(20)
t.left(90)
t.forward(160)






s.exitonclick()
