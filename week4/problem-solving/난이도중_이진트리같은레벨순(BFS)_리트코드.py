# Week4 코어타임 대비 문제풀이
# 링크 : https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # 루트가 비어있을 때
        if not root:
            return []

        answer = []
        queue = deque([root])

        while queue:
            current_level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            answer.append(current_level)

        return answer