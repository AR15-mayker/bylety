def calculate_average(numbers):
    if not numbers:
        return None

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average


numbers = [1, 2, 3, 4, 5]
average_value = calculate_average(numbers)
print(f"Среднее арифметическое чисел в массиве: {average_value}")
