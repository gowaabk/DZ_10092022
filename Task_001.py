""" 

    Задайте список из нескольких чисел. Напишите программу,
    которая найдёт сумму элементов списка, стоящих на нечётной позиции.

    Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
 """
import random


def sum_list(list1: list):  # Функция суммы нечетных позиций списка
    sum = 0
    for i in range(1, len(list1), 2):
        sum += list1[i]
    return sum


def create_random_list(list2: list, width: int):  # Функция генерации списка
    for i in range(width):
        list2.append(random.randint(0, width))
    return list2


N = int(input('Введите количество элементов в списке --> '))
list = []
list = create_random_list(list, N)
print(list)

print(sum_list(list))
