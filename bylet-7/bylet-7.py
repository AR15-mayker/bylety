def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


N = int(input("Введите количество чисел в последовательности Фибоначчи: "))
fib_seq = fibonacci_sequence(N)
print(f'Первые {N} число Фибоначчи:', ', '.join(map(str, fib_seq)))
