import pytest

from mypkg.my_answers import isPalindrome

def test_example1():
    s = "A man, a plan, a canal: Panama"
    assert(isPalindrome(s))


def test_example2():
    s = "race a car"
    assert(not isPalindrome(s))


def test_case1():
    s = "redivider"
    assert(isPalindrome(s))


def test_case2():
    s = "stevens"
    assert(not isPalindrome(s))


def test_case3():
    s = "Sir, I demand, I am a maid named Iris"
    assert(isPalindrome(s))






