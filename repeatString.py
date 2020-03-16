class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        a = n // 2
        # 最长的子字符串 也是 n // 2
        while a > 0:
            if n % a == 0:
                m = n // a
                # 获取该长度字符串 对应整体长度的倍数
                if s == s[:a] * m:
                    return True
            # 每次前进一个字符串
            a -= 1
        return False
