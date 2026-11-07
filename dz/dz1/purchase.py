def print_red(str):
    print("\033[31m" + str + "\033[0m")

print("сколько стоит батончик?")
price_print = input()
price_print = price_print.replace(",", ".")
price = float(price_print)

print("сколько штук?")
kol =  int(input())

summa = price * kol

print()
if summa > 0:
    print(f"Вам придется заплатить - {summa:.2f} рублей.")
else:
    print_red("бесплатно!")


