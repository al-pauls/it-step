import turtle
window = turtle.Screen()
t = turtle.Pen()
t.speed(0)
turtle.onscreenclick(t.setpos)
turtle.done() # Чтобы не закрывалось окно в PyCharm