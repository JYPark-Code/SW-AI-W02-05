"""
각 토핑을 넣거나/안넣거나 선택할 수 있다.
가능한 모든 피자 조합을 구하라. (아무것도 안 넣는 것 포함)

Example 1:
Input: toppings = [페퍼로니, 치즈, 올리브]
Output: [
  [],
  [페퍼로니],
  [치즈],
  [올리브],
  [페퍼로니, 치즈],
  [페퍼로니, 올리브],
  [치즈, 올리브],
  [페퍼로니, 치즈, 올리브]
]

Example 2:
Input: toppings = [햄, 파인애플]
Output: [[], [햄], [파인애플], [햄, 파인애플]]

프로그래밍 구조
선택
재귀
취소

미선택
재귀
"""
import sys
input = sys.stdin.readline
# AutoCP 한글 깨짐 CP949 -> UTF-8로 변경
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

toppings = list(input().split())
result = []

def backtrack(index, path):

    # base condition
    if index == len(toppings):
        result.append(path[:])
        return
    # backtrack

    # 넣는다.
    path.append(toppings[index])
    backtrack(index+1, path)
    path.pop()

    # 안넣는다.
    backtrack(index+1, path)

backtrack(0,[])
result.reverse()
print(result)