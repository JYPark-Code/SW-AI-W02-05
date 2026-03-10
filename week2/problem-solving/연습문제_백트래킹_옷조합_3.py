"""
상의, 하의, 신발에서 각각 하나씩 골라 코디를 완성하라.

Example 1:
Input:
  tops = [흰셔츠, 검정셔츠]
  bottoms = [청바지, 면바지, 반바지]
  shoes = [운동화, 구두]
Output: [
  흰셔츠-청바지-운동화, 흰셔츠-청바지-구두,
  흰셔츠-면바지-운동화, 흰셔츠-면바지-구두,
  흰셔츠-반바지-운동화, 흰셔츠-반바지-구두,
  검정셔츠-청바지-운동화, 검정셔츠-청바지-구두,
  검정셔츠-면바지-운동화, 검정셔츠-면바지-구두,
  검정셔츠-반바지-운동화, 검정셔츠-반바지-구두
]

Example 2:
Input:
  tops = [티셔츠]
  bottoms = [반바지]
  shoes = [슬리퍼, 샌들]
Output: [티셔츠-반바지-슬리퍼, 티셔츠-반바지-샌들]
"""
import sys
input = sys.stdin.readline
# AutoCP 한글 깨짐 CP949 -> UTF-8로 변경
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

tops = list(input().split())
bottoms = list(input().split())
shoes = list(input().split())

result = []

categories = [tops, bottoms, shoes]

def backtrack(start, path):

    if len(path) == len(categories):
        result.append("-".join(path))
        return

    current_category = categories[start]
    for item in current_category:
        path.append(item)
        backtrack(start+1 , path)
        path.pop()

backtrack(0, [])

print(result)




