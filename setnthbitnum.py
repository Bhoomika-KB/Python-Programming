# -*- coding: utf-8 

#Write a program to set nth bit of a number.

num=42
n_bit=1
binnum=bin(num).replace('0b',' ')

l=[]
for i in binnum:
    l.append(i)
if l[-(n_bit)]=='0':
    l[-(n_bit)]='1'
    
str1=''
for ele in l:
    str1=str1+ele
    
print(str1)