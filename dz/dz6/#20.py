kurs = float(input("сколько стоит 1$?"))

def converter(ruble):
    return ruble/kurs
print()
ruble = float(input('Сколко рулейй вы хотите поменять?'))
print()
print("Вы получите", converter(ruble), 'доларов')
