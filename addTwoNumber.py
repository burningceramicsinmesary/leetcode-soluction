import typing
import unittest


class ListNode:

    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __str__(self):
        nums = self.transfer_list()
        return " -> ".join([str(num) for num in nums])

    @classmethod
    def set_from_list(cls, nums: typing.List[int]) -> 'ListNode':
        head = cls(nums[0])
        prev = head
        for num in nums[1:]:
            prev.next = cls(num)
            prev = prev.next
        return head

    def transfer_list(self) -> typing.List[int]:
        nums = []
        tem = self
        while tem.next:
            nums.append(tem.val)
            tem = tem.next
        nums.append(tem.val)
        return nums


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        perv = result
        carry = 0
        while l1.next or l2.next:
            new_value, carry = (l1.val + l2.val + carry) % 10, int((l1.val + l2.val + carry) / 10)
            perv.next = ListNode(new_value)
            perv = perv.next
            if l1.next is None and l2.next is None:
                break
            else:
                if not (l1.next is None and l1.val == 0):
                    l1 = ListNode(0) if l1.next is None else l1.next
                if not (l2.next is None and l2.val == 0):
                    l2 = ListNode(0) if l2.next is None else l2.next

        new_value, carry = (l1.val + l2.val + carry) % 10, int((l1.val + l2.val + carry) / 10)
        perv.next = ListNode(new_value)
        if carry:
            perv.next.next = ListNode(carry)

        return result.next


class TestSolution(unittest.TestCase):

    def test_add_two_nums(self):
        test_data = [
            {
                "input": [[1, 2, 3, 4], [2, 3, 4, 5]],
                "output": [3, 5, 7, 9]
            },
            {
                "input": [[9, 2, 3, 4], [2]],
                "output": [1, 3, 3, 4]
            },

        ]
        solution = Solution()
        for data in test_data:
            input_data, out_data = data["input"], data["output"]
            with self.subTest():
                self.assertEqual(
                    solution.add_two_numbers(ListNode.set_from_list(input_data[0]),
                                             ListNode.set_from_list(input_data[1])
                                             ).transfer_list(),
                    out_data
                )

if __name__ == '__main__':
    unittest.main()
