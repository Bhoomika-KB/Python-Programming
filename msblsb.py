# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:13:31 2020

@author: RAJ KAMAL B GOWDA
"""

#Write a program to check Least Signifiant Bit (LSB) of a number is set or not and MSB of a number is set or not?

num=35
n_bit=4
y=binnum=bin(num).replace('0b',' ')

if y[0]=='1':
    print('lsb is set')
else:
    print('lsb is not set')
    
if y[-1]=='1':
    print('msb is set')
else:
    print('msb is not set')
    

