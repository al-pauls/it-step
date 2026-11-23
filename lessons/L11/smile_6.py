import smilic

x = 200
y = 200
for k in range(4):
    y = y - 75
    x = x - 70
    smilic.draw_smile(x, y)
for k in range(3):
    y = y - 70
    x = x + 75
    smilic.draw_smile(x, y)