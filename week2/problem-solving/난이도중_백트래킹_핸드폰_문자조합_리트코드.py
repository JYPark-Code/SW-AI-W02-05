# LeetCode Top Interview 150 : 17. Letter Combinations of a Phone Number
# 문제 링크 : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

# 백트래킹 문제 But 카타시안 곱이 떠올라서 2가지 방법으로 풀었다.
from itertools import product
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_string_dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                             "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                             "9": ["w", "x", "y", "z"]}

        if not digits:
            return []

        # groups = [phone_string_dict[d] for d in digits]

        # return [''.join(chars) for chars in product(*groups)]

        # Backtracking
        result = []
        curr = []

        def backtrack(index):

            if index == len(digits):
                result.append("".join(curr))
                return

            digit = digits[index]

            for ch in phone_string_dict[digit]:
                curr.append(ch)
                backtrack(index + 1)
                curr.pop()

        backtrack(0)
        return result





