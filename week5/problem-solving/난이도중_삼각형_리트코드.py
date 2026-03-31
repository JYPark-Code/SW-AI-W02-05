# 코어타임 4
# 링크 : https://leetcode.com/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]

        length = len(triangle)

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]