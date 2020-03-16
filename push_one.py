from typing import List
class Solution:
    def plusOne(self, digits:List[int]) -> List[int]:
        value = "".join([str(i) for i in digits]).lstrip("0")
        value = value if value else 0
        result_string = str(int(value) + 1)
        list_value = []
        for i in result_string:
            list_value.append(int(i))
        return list_value
