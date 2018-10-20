#!/usr/bin/python

"""
Python Functions and Recursions
"""


"""
QUESTION 1: 

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.

"""


def generateParenthesis(n):
    res = []

    def dfs(s, l, r):
        if len(s) == 2 * n: res.append(s)
        if l < n:
            dfs(s + "(", l + 1, r)
        if r < l:
            dfs(s + ")", l, r + 1)

    dfs("", 0, 0)
    return res


"""
QUESTION 2: 
========================================================================================================

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
=========================================
Input: "race a car"
Output: false

Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""


def isPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True