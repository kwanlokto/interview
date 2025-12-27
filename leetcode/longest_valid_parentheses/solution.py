def longest_valid_parentheses(s: str) -> int:
    # Stack to keep track of all open parentheses indices and the index of the most recent
    # unmatched ')' OR the base index before the start of a valid substring
    stack = [-1]
    longest = 0
    for idx, char in enumerate(s):
        if char == "(":
            stack.append(idx)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(idx)
            else:
                longest = max(longest, idx - stack[-1])
    return longest
