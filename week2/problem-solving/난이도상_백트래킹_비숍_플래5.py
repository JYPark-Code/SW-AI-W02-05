# 백트래킹 - 비숍 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1799

"""
문제
서양 장기인 체스에는 대각선 방향으로 움직일 수 있는 비숍(bishop)이 있다.
< 그림 1 >과 같은 정사각형 체스판 위에 B라고 표시된 곳에 비숍이 있을 때
비숍은 대각선 방향으로 움직여 O로 표시된 칸에 있는 다른 말을 잡을 수 있다.

그런데 체스판 위에는 비숍이 놓일 수 없는 곳이 있다.
 < 그림 2 >에서 체스판에 색칠된 부분은 비숍이 놓일 수 없다고 하자.
 이와 같은 체스판에 서로가 서로를 잡을 수 없도록 하면서 비숍을 놓는다면
 < 그림 3 >과 같이 최대 7개의 비숍을 놓을 수 있다.
색칠된 부분에는 비숍이 놓일 수 없지만 지나갈 수는 있다.

정사각형 체스판의 한 변에 놓인 칸의 개수를 체스판의 크기라고 한다.
체스판의 크기와 체스판 각 칸에 비숍을 놓을 수 있는지 없는지에 대한 정보가 주어질 때,
서로가 서로를 잡을 수 없는 위치에
놓을 수 있는 비숍의 최대 개수를 구하는 프로그램을 작성하시오.
"""
"""
board[r][c] == 1 인 칸만 후보

충돌 체크는 대각선 2개만

후보 칸들을 (r+c)%2 기준으로 둘로 나눠서 탐색량을 줄임

여기서부터는 이렇게 잡으면 됩니다.

보드를 돌면서 1인 칸만 모은다.

그 칸을 black_candidates, white_candidates로 나눈다.

각각에 대해 백트래킹한다.

답은 black_max + white_max (체스판이 체크 모양인 것을 말하는 것)
"""


import sys
input = sys.stdin.readline

n = int(input())

chessboard = [list(map(int, input().split())) for x in range(n)]
answer = 0
used_diag1 = [False] * (2*n)
used_diag2 = [False] * (2*n)
chess_black = []
chess_white = []


# 가능한 후보 만들기
for r in range(n):
    for c in range(n):
        if chessboard[r][c] == 1:
            if (r + c) % 2 == 0:
                chess_black.append((r, c))
            else:
                chess_white.append((r, c))

def dfs(candidate, idx, count):
    global answer
    if idx == len(candidate):
        answer = max(answer, count)
        return

    r, c = candidate[idx]

    d1 = r - c + (n - 1)
    d2 = r + c
    # 1) 놓을 수 있으면 놓기
    if not used_diag1[d1] and not used_diag2[d2]:

        # 체크
        used_diag1[d1] = True
        used_diag2[d2] = True

        dfs(candidate,idx+1, count+1)

        # 체크 해제
        used_diag1[d1] = False
        used_diag2[d2] = False

    # 2) 안 놓기
    dfs(candidate,idx+1, count)

dfs(chess_white,0,0)
white_answer = answer

answer = 0
used_diag1 = [False] * (2*n)
used_diag2 = [False] * (2*n)
dfs(chess_black,0,0)
black_answer = answer

print(white_answer + black_answer)

























