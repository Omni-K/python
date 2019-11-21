"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divider(a, b):
    if b == 0:
        print('Division by zero error')
        return 0
    else:
        if float(a/b).is_integer():
            return int(a/b)
        else:
            return a/b


first = int(input())
second = int(input())
print(divider(first, second))


