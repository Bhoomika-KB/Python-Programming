# -*- coding: utf-8 -*-


def decToBinary(n): 
      
    # Size of an integer is 
    # assumed to be 32 bits 
    for i in range(31, -1, -1):  
        k = n >> i; 
        if (k & 1): 
            print("1", end = ""); 
        else: 
            print("0", end = ""); 
  
   
n = 32; 
decToBinary(n); 