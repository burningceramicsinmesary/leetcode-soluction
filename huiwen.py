class Solution:

    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return True
        hash_map = {}
        for a in s:
            if a in hash_map.keys():
                hash_map[a] += 1
            else:
                hash_map[a] = 1
        odd_number = sum([1 for _,value in hash_map.items() if value %2 !=0])
        if odd_number >= 2 :
            return False
        return True
