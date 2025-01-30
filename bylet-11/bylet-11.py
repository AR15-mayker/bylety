def convert_c_to_f(celsius):
    return celsius * 9 / 5 + 32


def convert_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


while True:
    choice = input("Выберите действие:\n"
                   "1. Конвертировать из Цельсия в Фаренгейт\n"
                   "2. Конвертировать из Фаренгейта в Цельсий\n"
                   "Q. Выход\n"
                   "Ваш выбор: ").upper()

    if choice == 'Q':
        print("До свидания!")
        break

    try:
        temp = float(input("Введите температуру: "))
    except ValueError:
        print("Ошибка: введите корректное значение температуры.")
        continue

    if choice == '1':
        result = convert_c_to_f(temp)
        print(f"{temp:.2f}C = {result:.2f}F")
    elif choice == '2':
        result = convert_f_to_c(temp)
        print(f"{temp:.2f}F = {result:.2f}C")
    else:
        print("Ошибка: выберите корректное действие.")
