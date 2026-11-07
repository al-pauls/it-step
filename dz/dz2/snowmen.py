import turtle

window = turtle.Screen()
window.bgcolor("blue")

t = turtle.Pen()
t.shape("turtle")
t.pensize(35)
t.speed(2)

# малый круг
t.teleport(0,120)
t.color("pink")
t.circle(30)
# средний круг
t.teleport(0,0)
t.color("yellow")
t.circle(60)
#большой круг
t.teleport(0,-180)
t.color("green")
t.circle(90)



