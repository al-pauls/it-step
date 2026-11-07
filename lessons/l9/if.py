number = 23
guess = int(input("Введите число. "))
answer = guess - number
answer2 = number - guess
if guess == number:
    print("поздравляю, вы угадали!")
elif guess < number:
    print(f"Нет, загаданное число больше этогo на {answer:2f}")
else:
    print(f"Нет, загаданное число менньше этого на {answer:2f} ")