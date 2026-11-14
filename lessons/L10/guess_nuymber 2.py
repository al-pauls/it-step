import random
attempt = 1
number = random.randint(1, 100)
print("Компьютер загадал число в диапазоне от 1 до 100")
print("Желаете угадать число?")
guess = int(input("ВВедите число от 1 до 100:"))
while guess != number :
    if guess > number :
        print(guess, "Слишком велико.Попробуйте снова")
    if guess < number :
        print(guess,"Слишком мало.Попробуйте снова")
    guess = int(input("ВВедите число от 1 до 100:"))
    attempt = attempt + 1
print( guess, "- правильное число.Вы угадали!")
print(attempt,"попыток")