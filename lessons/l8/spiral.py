import turtle
window = turtle.Screen()
t = turtle.Pen()
t.speed(0)
colors = ["red", "green", "blue", "yellow"]
for n in range(100):
    t.color(colors[n % 4])
    t.circle(n)
    t.left(118)