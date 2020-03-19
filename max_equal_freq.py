from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        length_nums = len(nums)
        for i in range(-1, -1 * length_nums, -1):
            hash_map_dict = {}
            for key, value in hash_map.items():
                if value in hash_map_dict:
                    hash_map_dict[value] += 1
                else:
                    hash_map_dict[value] = 1
            if len(hash_map_dict) == 1:
                if hash_map_dict.get(1):
                    return length_nums + i + 1
            if len(hash_map_dict) == 2:
                if hash_map_dict.get(1) == 1:
                    return length_nums + i + 1
                max_value = max(hash_map_dict.keys())
                min_value = min(hash_map_dict.keys())
                if max_value - min_value == 1 and (hash_map_dict[max_value] == 1 or hash_map_dict[min_value] == 1):
                    return length_nums + i + 1
            if hash_map[nums[i]] - 1 == 0:
                hash_map.pop(nums[i])
            else:
                hash_map[nums[i]] -= 1
        else:
            return 0


print(Solution().maxEqualFreq([1,1]))
