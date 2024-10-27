import math

# Ввод целых чисел
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

# Проверка, чтобы избежать деления на ноль
denominator = 7 - (z % y)
if denominator == 0:
    print("Знаменатель f равен нулю. На ноль делить нельзя!.")
else:
    # Вычисление f и округление до трех знаков после запятой
    f = round(math.pow((x**5 + 7) / abs(-6 * y), 1/3) / denominator, 3)
    print("Результат:", f)
