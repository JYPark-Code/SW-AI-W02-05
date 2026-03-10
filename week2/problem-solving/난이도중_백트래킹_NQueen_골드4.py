# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
"""
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력
8

예제 출력
92
"""

"""
전락: 

1. 각 행마다 하나씩 놓기
2. 가능하면 다음 행에 가기 (안되면 X)
3. 끝까지 가서 n개 놓으면 종료

extra:
4. 1차원 배열로 충분 (2차원 X)

"""
import sys
input = sys.stdin.readline

n = int(input())

# col[row] = col
col = [-1] * n

answer = 0

used_col = [False] * n
used_diag1 = [False] * (2*n)
used_diag2 = [False] * (2*n)

def backtrack(row):
    global answer
    if row == n:
        answer += 1
        return

    for c in range(n):

        d1 = row - c + (n - 1)
        d2 = row + c

        if used_col[c] or used_diag1[d1] or used_diag2[d2]:
            continue

        used_col[c] = True
        used_diag1[d1] = True
        used_diag2[d2] = True

        backtrack(row + 1)

        used_col[c] = False
        used_diag1[d1] = False
        used_diag2[d2] = False


backtrack(0)
print(answer)
