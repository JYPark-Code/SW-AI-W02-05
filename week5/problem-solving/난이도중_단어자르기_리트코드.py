# 코어 타임 3
# 링크 : https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)

        len_str = len(s) + 1

        dp = [False] * len_str
        dp[0] = True

        for i in range(len_str):
            for j in range(0, i):
                if dp[j] is True and s[j:i] in wordDict_set:
                    dp[i] = True

        # print(dp)

        return dp[-1]
