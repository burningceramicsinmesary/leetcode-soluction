class Solution:

    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        valid_string = "qwertyuiopasdfghjklzxcvbnm1234567890"
        valid = "".join([i.lower() for i in s if i.lower() in valid_string])
        i, j = 0, len(valid) - 1
        while i < j:
            if valid[i] != valid[j]:
                return False
            i, j = i + 1, j - 1
        return True

print(Solution().isPalindrome("ababa"))
