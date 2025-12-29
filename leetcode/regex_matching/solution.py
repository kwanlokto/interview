"""
* -> >= 0 of the preceding element
a* -> no a, 1+ a
. -> Any element

"""


def is_regex_matching(s: str, p: str) -> bool:
    # dp[i][j] = does s[:i] match p[:j]
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    # Handle empty string with patterns like a*, a*b*
    for j in range(2, len(p) + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                # normal char match
                dp[i][j] = dp[i - 1][j - 1]

            elif p[j - 1] == "*":
                # zero occurrences
                dp[i][j] = dp[i][j - 2]

                # one or more occurrences
                if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[len(s)][len(p)]
