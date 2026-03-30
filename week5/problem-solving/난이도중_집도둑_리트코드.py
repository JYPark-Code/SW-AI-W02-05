# 코어 타임 2 , 링크 : https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rob(self, nums: List[int]) -> int:
        k = len(nums)
        dp = [0] * k

        dp[0] = nums[0]
        if k > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]