'''
Задача 2. Zip
Даны список букв (letters) и список цифр (numbers). Каждый список состоит из N
элементов. Создайте кортежи из пар элементов списков и запишите их в список
results. Не используйте функцию zip. Решите задачу в одну строку (не считая
print(results)).
Примеры списков:
letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
Результат работы программы:
[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]'''

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result_1 = [(letters[i], numbers[i]) for i in range(len(letters))]
print(result_1)

result_2 = list(map(lambda let, num: (let, num), letters, numbers))
print(result_2)