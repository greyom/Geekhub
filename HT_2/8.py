"""
Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа,
а значення для цих ключів - це квадрат ключа.
"""
num = int(input("Enter positive number: "))
dict_1 = {i : i**2 for i in range(num+1)}
print(dict_1)