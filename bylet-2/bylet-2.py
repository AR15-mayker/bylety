
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))


max_number = a

if b > max_number:
    max_number = b

if c > max_number:
    max_number = c

print(f"Максимальное число: {max_number}")
