# 링크 : https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # basic key

        word_dict = {}

        for word in strs:
            count = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            signature = tuple(count)

            if signature not in word_dict:
                word_dict[signature] = []

            word_dict[signature].append(word)

        return list(word_dict.values())