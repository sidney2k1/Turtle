import turtle
turtle.Screen().bgcolor("violet")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
number=4
length=70
angle=360/number
for i in range(number):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()