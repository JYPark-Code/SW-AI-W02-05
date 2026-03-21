# Week4 코어타임 대비 문제풀이
# 링크 :  https://leetcode.com/problems/binary-tree-right-side-view/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        result = []

        if root is None:
            return result

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # 맨 끝지점만 더하면 됨
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result