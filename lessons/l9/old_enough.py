driving_age = int(input("Какой минимальный возрастдля получения прав?"))
your_age = int(input("Сколько вам лет?"))
left = driving_age - your_age
if your_age >= driving_age:
    print("Вы уже достаточно взрослый для получения прав!")
else:

    print(f"Извините, вы не сможете еще в течение -{left: 2f} лет")