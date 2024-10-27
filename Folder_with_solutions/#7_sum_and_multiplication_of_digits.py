def sum_and_product_of_digits(n):
    digits = [int(digit) for digit in str(n)]

    sum_digits = sum(digits)
    prod_digits = 1
    for digit in digits:
        prod_digits *= digit

    return sum_digits, prod_digits


number = int(input("Введите двузначное или трехзначное число: "))

# Проверяем, что число двузначное или трехзначное
if 10 <= number <= 999:
    sum_digits, prod_digits = sum_and_product_of_digits(number)
    print(f"Сумма цифр: {sum_digits}")
    print(f"Произведение цифр: {prod_digits}")
else:
    print("Введите двузначное или трехзначное число!")
