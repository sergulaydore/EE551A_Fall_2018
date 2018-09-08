import pytest

from mypkg.my_answers import lists

p, r, c, d, o = lists()

def test_split():
    assert(p[0] == "Stevens")
    assert(p[1] == "is")
    assert(p[2] == "awesome")


def test_slice():
    assert(r=="wesome")


def test_last_row():
    assert(c[0] == 5)
    assert(c[1] == 11)
    assert(c[2] == 38)


def test_diagonal():
    assert(d[0]==10)
    assert(d[1]==38)


def test_ord():
    x = [chr(x) for x in o]
    rec = "".join(x)
    assert(rec == "Stevens")
