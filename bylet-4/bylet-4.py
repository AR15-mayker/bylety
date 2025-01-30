def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


Number = int(input("Введите положительное целое число: "))
try:
    fact = factorial(Number)
    print(f"{Number}! = {fact}")
except ValueError as e:
    print(e)
