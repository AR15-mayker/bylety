def linear_search(array, target):
    for i, value in enumerate(array):
        if value == target:
            return i
    return -1


array = [10, 20, 30, 40, 50]
target = 30
index = linear_search(array, target)

if index != -1:
    print(f"Элемент {target} найден на позиции {index}.")
else:
    print(f"Элемент {target} не найден.")
