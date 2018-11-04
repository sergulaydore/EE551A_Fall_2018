#!/usr/bin/python

"""
Object Oriented Programming and Python Classes
"""

"""
QUESTION 1: 
========================================================================================================
Write a class with name WindowAverage which is initialized by a window size and returns an average of
a stream of integers over a window by calling a method next. 

Example:
===========================
    w = WindowAverage(2)
    w.next(2) = 2
    w.next(4) = (2+4)/2
    w.next(3) = (4+3)/2
    w.next(2) = (2+3)/2
    
Hints: You should have __init__ and next methods and can use a data structure - double-ended queue
from collections module.    
"""

"""
QUESTION 2: 
========================================================================================================
Write a class with name AlternateIterator which is initialized by two lists v1 and v2
and returns the elements alternatively every time a method next is called and stops
iteration when both lists are exhausted

Example:
===========================
    Input: l1 = [1, 2, 3]
           l2 = [4, 5, 6, 7]
        
    Output: [1, 4, 2, 5, 3, 6, 7]
 
    Usage:
    iter = AlternateIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())

Hints: You should have three methods: __init__, next, and has_next. 
"""

"""
QUESTION 3:
========================================================================================================
Write a class ModifiedIterator that inherits the class AlternateIterator you wrote in Q2 that overwrites
the method next so that it return twice of the value from l2.

Example:
===========================
    Input: l1 = [1, 2, 3]
           l2 = [4, 5, 6, 7]
        
    Output: [1, 8, 2, 10, 3, 12, 14]
    
    Usage:
    iter = ModifiedIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())
"""




