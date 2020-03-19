class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)
        if needle_length > haystack_length:
            return -1
        if needle_length == haystack_length:
            if haystack == needle:
                return 0
            return -1
        for i in range(haystack_length-needle_length +1):
            if needle == haystack[i:i+needle_length]:
                return i
        return -1