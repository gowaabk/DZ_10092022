"""
    Напишите программу, которая найдёт произведение пар чисел списка.
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
 """
import random

# Функция генерации списка. Random от 0 до введенного N


def create_random_list(list2: list, width: int):
    for i in range(width):
        list2.append(random.randint(0, width))
    return list2

# Функция перемножения пар чисел


def mult_twix(list_mult: list):
    list_new = []
    # Проверка на четность/нечетность. Нужна для верного количества итераций.
    if len(list) % 2 == 0:
        length_half_list = len(list_mult)//2+1
    else:
        length_half_list = len(list_mult)//2+2

    for i in range(1, length_half_list):
        list_new.append(list_mult[i-1]*list_mult[-i])
    return list_new


N = int(input('Введите количество элементов в списке --> '))
list = []
list = create_random_list(list, N)
print('Сгенерированный список')
print(list)
print('Перемноженный список')
print(mult_twix(list))
