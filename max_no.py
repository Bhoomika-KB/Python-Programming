# -*- coding: utf-8 -*-


n1=int(input('Enter a first number:'))
n2=int(input('Enter a second number:'))
n3=int(input('Enter a third number:'))
if (n1>n2 and n1>n3):
    print(n1,'is greater')
elif (n2>n1 and n2>n3):
    print(n2,'is greater')
else:
    print(n3,'is greater')