from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        init_sanjiao = [[1]*(i+1) for i in range(numRows)]
        if numRows <= 2:
            return init_sanjiao
        for i in range(2, numRows):
            for j in range(1, i ):
                init_sanjiao[i][j] = init_sanjiao[i-1][j-1] + init_sanjiao[i-1][j]
        return init_sanjiao

