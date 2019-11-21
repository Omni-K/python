# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:16:35 2019

@author: Николай

Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
season_list = ['зима','весна','лето','осень']


season_dict = {0:'зима',
               1:'весна',
               2:'лето',
               3:'осень'}
month = int(input())
season = (month%12)//3
print('List variant:', season_list[season])
print('Dict variant:', season_dict[season])