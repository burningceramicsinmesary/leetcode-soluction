import typing
class Solution:

    def maxArea(self, height: typing.List[int]) -> int:
        start, end, area = 0 , len(height) -1, 0
        while start < end:
            # 如果 右边的桶高于左边的桶， 那我们需要尝试更高的桶壁从右边
            if height[start] < height[end]:
                area = max(area, height[start] * (end - start))
                start += 1
            else:
                area = max(area, height[end] *(end - start))
                end -= 1
        return area