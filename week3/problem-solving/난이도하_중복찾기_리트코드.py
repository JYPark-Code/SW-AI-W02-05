# 링크 : https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)

        if len(nums) == len(set_nums):
            return False

        else:
            return True
