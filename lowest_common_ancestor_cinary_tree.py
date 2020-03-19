from typing import List
from collections import deque
class TreeNode:

    def __init__(self, x:int):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def from_list(cls, nums: List[int]) -> 'TreeNode':
        # 构建顶点
        head = TreeNode(nums[0])
        queue = deque([head])
        tree_length = len(nums)
        i = 1
        # 循环整个列表
        while i < tree_length:
            # 如果还有 node 则为其设置左右节点
            node = queue.popleft()
            # 如果已经检测到左节点不存在了，则不再读取
            if node:
                # 先设置 左节点
                node.left = TreeNode(nums[i]) if nums[i] else None
                queue.append(node.left)
                if nums + 1 < tree_length:
                    # 设置右节点
                    node.right = TreeNode(nums[i+1]) if nums[i+1] else None
                    # 就算是 None 也要添加进去的原因，是为了保证数据的正确读取
                    queue.append(node.right)
                    # 如果成功设置右节点，则将其列表位置 向前加 1
                    nums +=1
                nums +=1
        return head

class SolutionBinaryTree:
    def lowestCommonAncestor(self, root:'TreeNode', p:'TreeNode', q:'TreeNode') -> TreeNode:
        """
        二叉树的最近公共祖先
        """
        if (root is None or root == p or root == q):
            return root
        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p ,q)
        if left is None:
            return right
        if right is None:
            return left


class SolutionBinarySearchTree:
    def lowestCommonAncestor(self, root:'TreeNode', p:'TreeNode', q:'TreeNode') -> TreeNode:
        """
        二叉搜索树的最近公共祖先
        """
        if root is None or root ==p or root == q:
            return root
        if p.val <= root.val <= q.val:
            return root
        elif root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestor(root.right, p, q)
        else:
            root = self.lowestCommonAncestor(root.left, p , q)
        return root

    def method_two(self, root:'TreeNode', p:'TreeNode', q:'TreeNode') -> TreeNode:
        while root:
            if p.val > root.val < q.val:
                root = root.right
            elif p.val < root.val > q.val:
                root = root.left
            else:
                return root
