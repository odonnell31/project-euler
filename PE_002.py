# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:14:45 2020

@author: ODsLaptop
"""
'''
ProjectEuler.net -- Problem 2

    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
'''

def fibonacci_sums(term1, term2, sum_of_evens, max_value):
    # sum terms 1 and 2 to get the new term
    new_term = term1 + term2
    
    # reset the values of term1 and term2
    term1 = term2
    term2 = new_term
    
    # add to the total sum of evens
    new_sum_of_evens = sum_of_evens
    if term2 % 2 == 0:
        new_sum_of_evens = sum_of_evens + term2
    
    if (term1+term2) < max_value:
        #print(term2, new_sum_of_evens, " going again!")
        fibonacci_sums(term1, term2, new_sum_of_evens, max_value)
        
    else:
        print("highest term:", term2, ",sum of even fib numbers:", new_sum_of_evens)
        

fibonacci_sums(1, 2, 2, 4000000)