#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:53:32 2022

@author: priteesinha
"""
a=int(input("Enter 1st num :"))
b=int(input("Enter 2nd num :"))
def gcd(a,b):
    if a>b:
        pass
    else: 
        a,b=b,a
    r=a%b
    while r!=0:
         a=b
         b=r
         r=a%b
    print ("GCD is :",b)
gcd(a,b)