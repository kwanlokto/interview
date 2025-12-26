"""
Problem Description
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.


Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
"""


def longest_valid_parentheses(s: str) -> int:
    return 0


assert longest_valid_parentheses("()") == 2
assert longest_valid_parentheses(")(") == 0
assert longest_valid_parentheses("(()") == 2
assert longest_valid_parentheses(")()())") == 4
assert longest_valid_parentheses("") == 0
assert longest_valid_parentheses("))((())") == 4
assert longest_valid_parentheses(")())()()") == 4