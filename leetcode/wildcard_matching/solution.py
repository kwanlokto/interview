def is_wildcard_matching(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True  # "" is a match with ""
    # Handle leading '*' matching empty string
    for j in range(len(p)):
        if p[j] == "*":
            dp[0][j + 1] = dp[0][j]

    for s_idx in range(len(s)):
        s_char = s[s_idx]

        for p_idx in range(len(p)):
            p_char = p[p_idx]

            if p_char == s_char or p_char == "?":
                dp[s_idx + 1][p_idx + 1] = dp[s_idx][p_idx]

            elif p_char == "*":
                dp[s_idx + 1][p_idx + 1] = (
                    dp[s_idx + 1][p_idx]  # match 0 characters
                    or dp[s_idx][p_idx + 1]  # match >= 1 characters
                )

    return dp[len(s)][len(p)]
