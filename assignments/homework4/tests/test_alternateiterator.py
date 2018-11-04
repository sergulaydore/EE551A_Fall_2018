import pytest

from mypkg.my_answers import AlternateIterator


def test_example():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7]

    iter = AlternateIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())

    assert(res == [1, 4, 2, 5, 3, 6, 7])

def another_example():
    l1 = [7, 12, 13, 17, 21]
    l2 = [1, 8, 27]

    iter = AlternateIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())

    assert(res == [7, 1, 12, 8, 13, 27, 17, 21])




