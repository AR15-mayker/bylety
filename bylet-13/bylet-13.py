def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


text = input("Введите текст: ")
vowel_count = count_vowels(text)
print(f"В тексте '{text}' содержится {vowel_count} гласных букв.")
