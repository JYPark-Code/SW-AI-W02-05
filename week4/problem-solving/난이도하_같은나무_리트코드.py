# Week4 코어타임 대비 문제풀이
# 링크 : https://leetcode.com/problems/same-tree/

# 같은 나무
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 둘다 비었으면 같다.
        if p is None and q is None:
            return True
        # 둘 중 하나만 비었으면 다르다.
        elif p is None or q is None:
            return False
        # 값이 다르면 다르다.
        elif p.val != q.val:
            return False
        # 좌,우 노드가 모두 같아야한다.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
