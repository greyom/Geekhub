"""
Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), 
кожен елемент якого буде ділитись без остачі на 5 але не буде ділитись на 3.
"""

values = [val for val in range(100) if val % 5 == 0 and val % 3 != 0]
print(values)