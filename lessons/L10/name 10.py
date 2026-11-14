import random
names = ["Маша","Коля","Саша","Влад","Дима"]
k = 0
while k <= 10:
    name = random.choice(names)
    print(name)
    k = k + 1