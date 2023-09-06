import re

sentence = input("Введите предложение: ")

# Используем регулярное выражение для поиска подряд идущих пробелов
spaces = re.findall(r'\s+', sentence)

if spaces:
    max_spaces = max(spaces, key=len)
    print(f"Наибольшее количество идущих подряд пробелов: {len(max_spaces)}")
else:
    print("В предложении нет пробелов.")