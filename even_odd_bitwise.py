# -*- coding: utf-8 -*-


num = int(input("Enter a number: "))    
# checking the number using bitwise operator
if num&1:                          
    print(num,"is an odd number.")    
else:
    print(num,"is an even number.")