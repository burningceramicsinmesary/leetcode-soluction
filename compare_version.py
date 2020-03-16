class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        version1_list = [int(item.lstrip("0") if item.lstrip("0") else 0) for item in version1.split(".")]
        version2_list = [int(item.lstrip("0") if item.lstrip("0") else 0) for item in version2.split(".")]
        version1_len, version2_len = len(version1_list), len(version2_list)
        allow_len = max(version1_len, version2_len)
        init_multi = 0
        version1_num, version2_num = 0, 0
        for i in range(allow_len):
            if i < version1_len:
                version1_num += version1_list[i] * (10 ** init_multi)
            if i < version2_len:
                version2_num += version2_list[i] * (10 ** init_multi)
            init_multi -= 1
        if version1_num == version2_num:
            flag = 0
        elif version1_num > version2_num:
            flag = 1
        else:
            flag = -1
        return flag


print(Solution().compareVersion("0.1", "1.0"))
print([item.lstrip("0") for item in "1.0".split(".")])
print("0".strip("0"))
a = [1,2]
print(a[1:])
