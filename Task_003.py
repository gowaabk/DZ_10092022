"""
    Задайте список из вещественных чисел.
    Напишите программу, которая найдёт
    разницу между максимальным и минимальным значением дробной части элементов.

    Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
 """


def part_minus(my_list: list):  # Функкция поиска разности мин и макс дробной части чисел в списке
    max_list = 0
    min_list = 1
    for i in range(len(my_list)):
        if (my_list[i])-int(my_list[i]) > max_list:
            max_list = (my_list[i])-int(my_list[i])
        elif (my_list[i])-int(my_list[i]) < min_list and ((my_list[i])-int(my_list[i]) != 0):
            min_list = (my_list[i])-int(my_list[i])
    return round((max_list-min_list), 5)


my_list = [1.1, 1.2, 3.23, 5, 10.01]


print(my_list)
print('Разница между максимальной и минимальной дробной частью чисел списка равна - ',
      part_minus(my_list))
