'''
Задача 3. Палиндром
Используя модуль collections, реализуйте функцию can_be_poly, которая
принимает на вход строку и проверяет, можно ли получить из неё палиндром.
'''

from collections import Counter


def can_be_poly(text: str) -> bool:
    letters_dict = Counter(text)
    resulst = list(filter(lambda x: x%2 ==1, letters_dict.values()))
    print(letters_dict, resulst)
    if len(resulst) in (0,1):
        return True 
    else:
        return False


s = 'adasfssfffdaasadfsdf'


print(can_be_poly(s))