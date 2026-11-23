import smilic

x = 0
y = 300
for i in range(5):
    y = y - 100
    smilic.draw_smile(x, y)