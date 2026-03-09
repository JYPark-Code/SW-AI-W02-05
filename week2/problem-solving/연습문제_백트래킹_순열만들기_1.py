"""
문제 1: 비밀번호 만들기
숫자 [1, 2, 3]으로 만들 수 있는 모든 3자리 비밀번호를 구하라.
각 숫자는 한 번씩만 사용 가능.

Example 1:
Input: nums = [1, 2, 3]
Output: [123, 132, 213, 231, 312, 321]

Example 2:
Input: nums = [1, 2]
Output: [12, 21]
"""

# n개 중에 k를 선택하는 것 - 한번 선택되어도 다시 선택 가능
nums = [1, 2, 3]
start = 1


def permutation(nums, k):
    result = []
    visited = [False] * len(nums)

    def backtrack(current_permutation):
        if len(current_permutation) == k:
            # result.append(current_permutation[:])
            result.append(int("".join(map(str, current_permutation))))
            return

        for i in range(len(nums)):
        # 1. 선택 - 2. 탐색 - 3. 취소
            if not visited[i]:
                visited[i] = True
                current_permutation.append(nums[i])
                backtrack(current_permutation)

                current_permutation.pop()
                visited[i] = False


    backtrack([])
    return result


print(permutation(nums, 3))

# -------------
"""
nums = input().split()
result = []

def backtrack(path):
    if len(path) == len(nums):
        result.append(int("".join(path)))
        return
    
    for num in nums:
        if num in path:
            continue
        
        path.append(num)
        backtrack(path)
        path.pop()

backtrack([])
print(result)
"""