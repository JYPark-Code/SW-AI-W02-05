"""
후보자들 중에서 k명을 뽑아 팀을 구성하라.
순서는 상관없음. (AB와 BA는 같은 팀)

Example 1:
Input: members = ['A', 'B', 'C', 'D'], k = 2
Output: ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']

Example 2:
Input: members = ['A', 'B', 'C'], k = 2
Output: ['AB', 'AC', 'BC']
"""

members = list(input().split())
k = int(input())

result = []

def backtrack(start, path):
    #  base case - k개를 모두 선택했으면 결과에 추가
    if len(path) == k:
        result.append("".join(path))
        # result.append(path[:])
        return
    #  처음부터 끝까지 element 하나씩 시도
    for i in range(start, len(members)):
    ##  백트랙킹 3단계 구현
    ## 1. 선택
        path.append(members[i])
    ## 2. 탐색
        backtrack(i+1, path)
    ## 3. 취소
        path.pop()

backtrack(0, [])
print(result)