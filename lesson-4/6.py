# -*- coding: utf-8 -*-
"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
def int_func(text=''):
    firstLetter = chr(ord(text[0])-32)
    return firstLetter+text[1:]

def make_It_Like_A_Title(text):
    a = text.split(' ')
    for idx, item in enumerate(a):
        a[idx] = int_func(item)
    return ' '.join(a)

print(make_It_Like_A_Title(input()))