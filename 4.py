# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:16:35 2019

@author: Николай
"""
a = int(input())
maxn = 0
while a!=0:
    n = a%10
    if n>maxn:
        maxn=n
    if maxn==9:
        break
    a//=10
print(maxn)
