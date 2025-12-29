"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""

def wildcard_matching(s: str, p: str) -> bool:
    return False

assert wildcard_matching("aa", "a") == False
assert wildcard_matching("aa", "*") == True 
assert wildcard_matching("cb", "?a") == False
assert wildcard_matching("adceb", "*a*b") == True