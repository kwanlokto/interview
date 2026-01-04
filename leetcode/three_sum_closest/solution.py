def three_sum_closest(nums: list[int], target: int) -> int:
    closest_target = None
    nums.sort()
    for i in range(len(nums) - 2):  # ignore 2 because we need one for j and k
        num_i = nums[i]
        j = i + 1
        k = len(nums) - 1
        while j < k:
            num_j = nums[j]
            num_k = nums[k]
            total = num_i + num_j + num_k
            if total < target:
                # Check to see if this is the closest we've seen
                if closest_target is None or abs(target - total) < abs(target - closest_target):
                    closest_target = total
                j += 1  # Needs to be more positive
            elif total > target:
                # Check to see if this is the closest we've seen
                if closest_target is None or abs(target - total) < abs(target - closest_target):
                    closest_target = total
                k -= 1  # Needs to be more negative
            else:
                return target
    return closest_target
                
