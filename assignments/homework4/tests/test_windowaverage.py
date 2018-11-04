import pytest

from mypkg.my_answers import WindowAverage


def test_window2():
    w = WindowAverage(2)
    assert(w.next(6) == 6)
    assert(w.next(8) == (6 + 8) / 2)
    assert (w.next(3) == (8 + 3) / 2)


def test_window3():
    w = WindowAverage(3)
    assert(w.next(1) == 1)
    assert(w.next(3) == (1 + 3)/2)
    assert(w.next(5) == (1 + 3 + 5)/3)
    assert(w.next(4) == (3 + 5 + 4)/3)



