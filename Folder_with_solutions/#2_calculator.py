import math

# Запрашиваем у пользователя два целых числа
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

print("Арифметические операции:")
print(f"{num1} + {num2} = {round(num1 + num2, 2)}")
print(f"{num1} - {num2} = {round(num1 - num2, 2)}")
print(f"{num1} * {num2} = {round(num1 * num2, 2)}")

if num2 != 0:
    print(f"{num1} / {num2} = {round(num1 / num2, 2)}")
    print(f"{num1} // {num2} = {round(num1 // num2, 2)}")
    print(f"{num1} % {num2} = {round(num1 % num2, 2)}")
else:
    print("Нельзя делить на 0!")

print(f"{num1} ** {num2} = {round(num1 ** num2, 2)}")

if num1 > 0:  # log10 определен только для положительных чисел
    print(f"log10({num1}) = {round(math.log10(num1), 2)}")
else:
    print("log10 не определен для неположительных чисел.")

# Сравнительные операции
print("\nСравнительные операции:")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} == {num2}: {num1 == num2}")
