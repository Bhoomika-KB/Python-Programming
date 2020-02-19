# -*- coding: utf-8 -*-

y= input('enter the binary numbers:').split(',')

for ele in y:
    if int(ele,2)%5==0:
        print(ele)