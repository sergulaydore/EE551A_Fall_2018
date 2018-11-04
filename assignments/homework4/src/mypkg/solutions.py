#!/usr/bin/python


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

from collections import deque


class WindowAverage(object):

    def __init__(self, size):
        """
        Initialize your class.
        :type size: int
        """
        self.size = size
        self.current = 0
        self.q = deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) < self.size:
            self.q.append(val)
            self.current = float(self.current * (len(self.q) - 1) + val) / len(self.q)

        else:
            removed = self.q.popleft()
            self.q.append(val)
            self.current = self.current + float(val - removed) / self.size

        return self.current


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


class AlternateIterator(object):

    def __init__(self, l1, l2):
        """
        Initialize class.
        :type l1: List[int]
        :type l2: List[int]
        """
        self.l1 = l1
        self.l2 = l2
        self.switch = 0

    def next(self):
        """
        :rtype: int
        """
        if self.l1 or self.l2:
            if self.switch == 0:
                self.switch ^= 1
                return self.l1.pop(0) if self.l1 else self.l2.pop(0)
            else:
                self.switch ^= 1
                return self.l2.pop(0) if self.l2 else self.l1.pop(0)

    def has_next(self):
        """
        :rtype: bool
        """
        if self.l1 or self.l2: return True
        return False


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


class ModifiedIterator(AlternateIterator):
    def next(self):
        """
        :rtype: int
        """
        if self.l1 or self.l2:
            if self.switch == 0:
                self.switch ^= 1
                return self.l1.pop(0) if self.l1 else 2 * self.l2.pop(0)
            else:
                self.switch ^= 1
                return 2 * self.l2.pop(0) if self.l2 else self.l1.pop(0)


if __name__ == "__main__":
    l1 = [7, 12, 13, 17, 21]
    l2 = [1, 8, 27]

    iter = ModifiedIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())

    print(res == [7, 2, 12, 16, 13, 54, 17, 21])



