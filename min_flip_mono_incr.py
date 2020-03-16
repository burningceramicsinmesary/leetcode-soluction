class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        s = S.lstrip("0")
        s = s.rstrip("1")
        if not s:
            return 0
        zero_number = 0
        one_number = 0
        for i in s:
            if i == "0":
                zero_number += 1
            else:
                one_number += 1
        return min(zero_number, one_number)

