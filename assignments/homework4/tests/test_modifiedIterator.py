import pytest

from mypkg.my_answers import ModifiedIterator


def test_example():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7]

    iter = ModifiedIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())

    assert(res == [1, 8, 2, 10, 3, 12, 14])

def another_example():
    l1 = [7, 12, 13, 17, 21]
    l2 = [1, 8, 27]

    iter = ModifiedIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())

    assert(res == [7, 2, 12, 16, 13, 54, 17, 21])







