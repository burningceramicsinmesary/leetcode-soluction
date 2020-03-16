from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]):
        nums_length = len(nums)
        max_sum = nums[0]
        for i in range(1, nums_length):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
        return max_sum
