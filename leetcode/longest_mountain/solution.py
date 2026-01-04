def longest_mountain(arr: list[int]) -> int:
    if len(arr) < 3:
        return 0

    max_mountain = 0
    left_count = 0
    right_count = 0

    for i in range(1, len(arr)):
        prev = arr[i - 1]
        curr = arr[i]
        if curr > prev:  # increasing
            if right_count > 0:
                max_mountain = max(max_mountain, left_count + right_count + 1)
                right_count = 0
                left_count = 0
            left_count += 1
        elif curr < prev and left_count > 0: # decreasing
            right_count += 1
        else:  # reset the count because we don't have a mountain
            if left_count > 0 and right_count > 0:  # we had a mountain before
                max_mountain = max(max_mountain, left_count + right_count + 1)
            left_count = 0
            right_count = 0

    if left_count > 0 and right_count > 0:
        max_mountain = max(max_mountain, left_count + right_count + 1)
    return max_mountain