# -*- coding: utf-8 -*-


n=int(input("Enter a number: "))
if(n%4==0)and(n % 100 != 0 or n % 400 == 0):
    print("Leap year")
else:
    print("Non Leap")