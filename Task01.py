'''
Задание 1. Новые списки
Даны три списка:
1. floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
2. names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
3. numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
Напишите код, который создаёт три новых списка. Вот их содержимое:
1. Каждое число из списка floats возводится в третью степень и округляется
до трёх знаков после запятой.
2. Из списка names берутся только имена минимум из пяти букв.
3. Из списка numbers берётся произведение всех чисел.
'''
from functools import reduce

list_float = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
list_str = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
list_int = [22, 33, 10, 6894, 11, 2, 1]

list_1 = list(map(lambda x: round(x**3, 3), list_float))
print(list_1)

list_2 = list(filter(lambda name: len(name) >= 5, list_str))
print(list_2)

list_3 = reduce(lambda x, y: x*y, list_int)
print(list_3)
