# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 08:12:36 2018

@author: ODsLaptop
"""

# natural numbers: positive whole integers

# find the sum of all the multiples of 3 and 5 below 1000

def NNSumBelowNum(num):
    num_sum = 0
    #num = (num/2) + 1
    num_range = range(1,num)
    
    for i in num_range:
        if (i%3 ==0) or (i%5 == 0):
            num_sum = num_sum+i
    print num_sum
    
NNSumBelowNum(1000)
#233168