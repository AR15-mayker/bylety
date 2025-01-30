import math


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    limit = int(math.sqrt(number)) + 1
    for i in range(5, limit, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


N = int(input("Введите число: "))
if is_prime(N):
    print(f"{N} — простое число.")
else:
    print(f"{N} — составное число.")
