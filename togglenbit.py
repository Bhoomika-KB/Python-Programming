# -*- coding: utf-8 -*-


#toggle nth bit of the number

num=24
n_bit=2
binnum=bin(num).replace('0b',' ')


lst=[]
for i in binnum:
    lst.append(i)
if lst[-(n_bit)]=='0':
    lst[-(n_bit)]='1'
else:
    lst[-(n_bit)]='0'

str1=''
for ele in lst:
    str1=str1+ele
print(str1)