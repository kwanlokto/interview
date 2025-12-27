import math

def min_swaps(s: str) -> int:
    # Check if balancing is possible
    balance = 0
    most_negative = 0
    for bracket in s:
        if bracket == "(":
            balance += 1
        elif bracket == ")":
            balance -= 1

        if balance < most_negative:
            most_negative = balance

    if balance == 0:
        return math.ceil(-most_negative / 2)
    return -1