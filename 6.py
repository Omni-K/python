# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:16:35 2019

@author: Николай
"""
a = float(input())
b = float(input())
s = a #общий результат спортсмена
day=1
while s<b:
    a*=1.1
    s+=a
    day+=1
print(day)


