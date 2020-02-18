# -*- coding: utf-8 -*-


def comp_gcd(a,b):
    if b==0:
        return a
    else:
        return(comp_gcd(b,a%b))
        
comp_gcd(30,250)