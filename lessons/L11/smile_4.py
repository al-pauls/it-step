import smilic

x = -400
y = -300
for i in range(4):
    y = y + 100
    x = x + 100
    smilic.draw_smile(x, y)