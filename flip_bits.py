# -*- coding: utf-8 -*-



import math 

def invertBits(num): 

	x = int(math.log2(num)) + 1

	for i in range(x): 
		num = (num ^ (1 << i)) 
	
	print(num) 

num = 11
invertBits(num) 

