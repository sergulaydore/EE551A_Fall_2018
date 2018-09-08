import pytest

from mypkg.my_answers import dictionaries

a, f, p, k = dictionaries()


def test_fruit():
    assert(a == "apple")


def test_quantity():
    assert(f["quantity"] == 5)


def test_programmer():
    assert(p == "programmer")


def test_sort():
    assert(k == ["age", "jobs", "name"])
