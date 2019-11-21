"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def printUserData(first_name='Unknown', second_name='Unknown', year_of_birth='неизвестно', city='неизвестно', email='неизвестно', tel='неизвестно'):
    print(f'имя: {first_name} фамилия: {second_name} год рождения: {year_of_birth} город проживания: {city} email: {email} телефон: {tel}')

printUserData(first_name='Иван',
              second_name='Петров',
              year_of_birth='1983',
              city='Москва',
              email='zhena@zhizni.net',
              tel='+79251234567')