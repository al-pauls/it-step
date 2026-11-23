import turtle
x = -300
y = 0
window = turtle.Screen()
window.bgcolor("blue")
t = turtle.Pen()
t.color("green")
t.pensize(30)
t.speed(0)
t.teleport(x, y)
#t.setpos(x, y)
turtle.onscreenclick(t.setpos)
turtle.done()