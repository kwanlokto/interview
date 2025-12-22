"""
Problem Description
Given a string s containing only the characters '(' and ')', return the minimum number of adjacent swaps needed to make the string balanced. If it's impossible to balance the string, return -1.
A string is balanced if:
Every opening parenthesis '(' has a corresponding closing parenthesis ')'
At no point while reading left to right does the count of closing parentheses exceed the count of opening parentheses

Example 1:
Input: s = "())(()"
Output: 1
Explanation: Swap indices 2 and 3: "())(()" -> "()()()"
The string becomes balanced after 1 swap.

Example 2:
Input: s = "))(("
Output: 1
Explanation: Swap indices 0 and 3: "))((" -> "()()"
Total: 1 swap

Example 3:
Input: s = "((()))"
Output: 0
Explanation: The string is already balanced.
"""


def min_swaps(s: str) -> int:
    return 0
