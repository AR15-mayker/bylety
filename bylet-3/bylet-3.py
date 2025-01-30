def sum_of_numbers_formula(n):
    return n * (n + 1) // 2


N = int(input("Введите число N: "))
result = sum_of_numbers_formula(N)
print(f"Сумма всех целых чисел от 1 до {N}: {result}")
