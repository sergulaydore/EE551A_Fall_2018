import pytest

from mypkg.my_answers import numbers_and_strings

x, y, z, length, m, n = numbers_and_strings()


def test_power():
    assert(x == 4072324)


def test_string():
    assert(y == "Stevens")


def test_repeat():
    assert(len(z) == 5 * len("Stevens"))


def test_len():
    assert(length == 35)


def test_concat():
    assert(m == "Stevens is good")


def test_replace():
    assert(n == "Stevens is awesome")
