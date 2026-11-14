import random
import turtle
window = turtle.Screen()
t = turtle.Pen()
number = random.randint(4,10)
window.title("Количество окружностей ="+str(number))
for i in range(number):
    radius =100
    color = "red"
    width = 5
    t.width(width)
    t.color(color)
    t.circle(radius)
    t.left(360/number)