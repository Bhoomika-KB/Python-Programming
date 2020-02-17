# -*- coding: utf-8 -*-


#Write a program to get nth bit of a input number.

def nbit(num,n_bit):
    y=bin(num).replace('0b','')
    print(y)
    return y[-(n_bit)]   

nbit(24,5)