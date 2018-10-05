#!/usr/bin/python

"""
Python Statements
"""


def add_binary(a, b):
    """
    This is to review binary operations
    ============================================================

    Given two binary strings, return their sum (also a binary string).

    Return None if one of the input strings are empty or contains characters different than 1 or 0.

    Example 1:
                Input: a = "11", b = "1"
                Output: result = "100"

    Example 2:
                Input: a = "1010", b = "1011"
                Output: result = "10101"
    """

    try:
        result = bin(int(a, 2) + int(b, 2))[2:]
    except:
        result = None

    return result


def plus_one(digits):
    """
    This is to review loops and if statements
    ============================================================

    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    You can do this in-place!

    The digits are stored such that the most significant digit is at the head of the list, and each
    element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.


    Example 1:
            Input: digits = [1, 2, 3]
            Output: digits = [1, 2, 4]
            Explanation: The array represents the integer 123.

    Example 2:
            Input: digits = [1, 0, 9, 9]
            Output: digits = [1, 1, 0, 0]
    """
    digits[-1] += 1
    tail = len(digits) - 1
    while digits[tail] == 10 and tail > 0:
        digits[tail] = 0
        digits[tail - 1] += 1
        tail -= 1
    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)

    return digits


def roman_to_integers(roman_string):
    """
    This is to review loops, if statements and dictionaries
    ============================================================

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, two is written as II in Roman numeral, just two one's added together.
    Twelve is written as, XII, which is simply X + II. The number twenty seven is written
    as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:

    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

    Example 1:
        Input: "III"
        Output: 3

    Example 2:
        Input: "IV"
        Output: 4

    Example 3:
        Input: "IX"
        Output: 9

    Example 4:
        Input: "LVIII"
        Output: 58
        Explanation: C = 100, L = 50, XXX = 30 and III = 3.

    Example 5:
        Input: "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    if len(roman_string) == 0:
        return my_dict[roman_string]
    else:
        prev_val = my_dict[roman_string[0]]
        integer += prev_val
        idx = 1
        while idx < len(roman_string):
            current_val = my_dict[roman_string[idx]]
            if current_val <= prev_val:
                integer += current_val
                prev_val = current_val
            else:
                integer += current_val - 2 * prev_val
                prev_val = current_val
            idx += 1
        return integer

