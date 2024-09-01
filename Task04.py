'''
Задача 4. Уникальный шифр
Напишите функцию, которая принимает строку и возвращает количество
уникальных символов в строке. Используйте для выполнения задачи
lambda-функции и map и/или filter.
Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
регистра должны считаться одинаковыми'''

message = "Today is a beautiful day! The sun is shining and the birds are singing."

def count_unique_chars(text: str) -> int:
    result = list(filter(lambda x: text.lower().count(x.lower()) == 1, text))
    return len(result)

unique_count = count_unique_chars(message)

print(f'Value if unique chars is {unique_count}')

