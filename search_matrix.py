from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        def acquire_column(matrix, target):
            prev_min_value = float('-inf')
            for column in matrix:
                if column:
                    min_value, max_value = column[0], column[-1]
                    if target == min_value:
                        return True
                    if prev_min_value < target < min_value:
                        return False
                    if target == max_value:
                        return True
                    if min_value < target < max_value:
                        return column
            return False
        column = acquire_column(matrix, target)
        def binarySearch(arr, l, r, x):
            if r >= l:
                mid = int(l + (r - l) / 2)
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    return binarySearch(arr, l, mid - 1, x)
                else:
                    return binarySearch(arr, mid + 1, r, x)
            else:
                return  -1
        if isinstance(column, list):
            if binarySearch(column, 0, len(column) -1 , target) == -1:
                return False
            return True
        else:
            return column

print(Solution().searchMatrix([[1,3]], 3))
