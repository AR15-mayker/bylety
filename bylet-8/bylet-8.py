def remove_duplicates(arr):
    return list(set(arr))


array = [1, 2, 3, 2, 4, 5, 3, 7, 9, 7]
unique_array = remove_duplicates(array)
print(unique_array)
