import pytest

from mypkg.my_answers import add_binary


def test_both_empty():
    result = add_binary('', '')
    assert(result == None)

def test_first_empty():
    result = add_binary('', '1010')
    assert(result == None)

def test_second_empty():
    result = add_binary('1010', '')
    assert(result == None)

def test_first_nonbinary():
    result = add_binary('1301', '1010')
    assert(result == None)

def test_second_nonbinary():
    result = add_binary('1010', '1301')
    assert(result == None)

def test_example1():
    result = add_binary('11', '1')
    assert(result=="100")

def test_example2():
    result = add_binary('1010', '1011')
    assert(result=="10101")

def test_case_1():
    result = add_binary('10101111', '010101')
    assert(result=='11000100')

def test_case2():
    result = add_binary('111', '101')
    assert(result=='1100')



