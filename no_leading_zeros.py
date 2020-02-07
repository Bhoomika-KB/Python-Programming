# -*- coding: utf-8 -*-




 
def countZeros(x): 
	
	total_bits = 32
	res = 0
	while ((x & (1 << (total_bits - 1))) == 0): 
		x = (x << 1) 
		res += 1

	return res 

x = 101
print(countZeros(x)) 

