"""     Напишите программу, которая будет преобразовывать десятичное число в двоичное.

    Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
 """


def bin_number(number):
    bin_num = ''
    while (number > 0):
        bin_num = str((number % 2)) + bin_num
        number = number // 2
    return bin_num


n = int(input('Введтие десятичное число --> '))
print(f'{n} в двоичной системе равно {bin_number(n)}')
