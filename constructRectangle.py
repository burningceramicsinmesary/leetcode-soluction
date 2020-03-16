from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        max_width = int(math.sqrt(area))
        if max_width * max_width == area:
            return [max_width, max_width]
        list_nums = []
        for i in range(1, max_width + 1):
            width = i
            if area %width == 0:
                length = int(area /width)
                list_nums.append([length, width])

        sort_list = sorted(list_nums, key= lambda a : a[0] - a[1])
        return sort_list[0]
