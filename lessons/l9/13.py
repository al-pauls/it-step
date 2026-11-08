import turtle
window = turtle.Screen()
t = turtle.Pen()
number = int(turtle.numinput("Количество сторон или окружностей", \
    "Сколько сторон или окружностей будет у фигуры?"))
shape = turtle.textinput("Какую фигурувы хотите?", \
    "Введите 'м'для многоугольника или'м' для розетки ")
for k in range(number):
    if shape == 'p':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360 / number)