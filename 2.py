# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:16:35 2019

@author: Николай
"""
secundo = int(input())
h = secundo//(60*60)
m = secundo//60 - h*60
s = secundo % 60
print("{:0>2}:{:0>2}:{:0>2}".format(h,m,s))
