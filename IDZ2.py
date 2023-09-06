sentence = input("Введите предложение: ")
search_char = 'а'

# Используем метод find() для поиска буквы 'а' в предложении
index = sentence.find(search_char)

if index != -1:
    print(f"Буква '{search_char}' найдена в предложении.")
    print(f"Порядковый номер первой буквы '{search_char}': {index + 1}")
else:
    print(f"Буква '{search_char}' не найдена в предложении.")
