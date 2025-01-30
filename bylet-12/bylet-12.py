def is_palindrome(s):
    return s == s[::-1]


string = input("Введите строку: ")
if is_palindrome(string):
    print(f'Строка "{string}" является палиндромом.')
else:
    print(f'Строка "{string}" не является палиндромом.')
