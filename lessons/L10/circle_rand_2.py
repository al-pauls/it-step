import random
import turtle
colors = ["red", "green", "blue","orange","brown","purple" ]
radius = 100
width = 5
number = random.randint(4,10)

window = turtle.Screen()
window.title("Количество окружностей ="+str(number))
t = turtle.Pen()

for i in range(number):
    color = random.choice(colors)
    t.width(width)
    t.color(color)
    t.circle(radius)
    t.left(360/number)