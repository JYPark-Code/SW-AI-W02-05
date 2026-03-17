# 링크 : https://leetcode.com/problems/top-k-frequent-words/description/
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        # 정렬
        sorted_words = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

        # 상위 k개만 추출
        answer = [word for word, count in sorted_words[:k]]

        return answer