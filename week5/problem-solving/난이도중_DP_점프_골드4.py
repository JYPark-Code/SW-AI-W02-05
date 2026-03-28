# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
"""
문제
N(2 ≤ N ≤ 10,000)개의 돌들이 같은 간격으로 놓여 있다. 편의상 순서대로 1, 2, …, N번 돌이라고 부르자.
당신은 현재 1번 돌 위에 있는데, 이 돌들 사이에서 점프를 하면서 N번째 돌로 이동을 하려 한다. 이때 다음 조건들이 만족되어야 한다.

이동은 앞으로만 할 수 있다. 즉, 돌 번호가 증가하는 순서대로만 할 수 있다.
제일 처음에 점프를 할 때에는 한 칸밖에 점프하지 못한다. 즉, 1번 돌에서 2번 돌이 있는 곳으로 점프할 수 있다.
그 다음부터는 가속/감속 점프를 할 수 있는데, 이전에 x칸 점프를 했다면,
다음번에는 속도를 줄여 x-1칸 점프하거나, x칸 점프하거나, 속도를 붙여 x+1칸 점프를 할 수 있다.
물론 점프를 할 때에는 한 칸 이상씩 해야 한다.
각 돌들은 각기 그 크기가 다르고, 그 중 몇 개의 돌은 크기가 너무 작기 때문에 당신은 그러한 돌에는 올라갈 수 없다.
위와 같은 조건들을 만족하면서 1번 돌에서 N번 돌까지 점프를 해 갈 때, 필요한 최소의 점프 횟수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 N, M(0 ≤ M ≤ N-2)이 주어진다. M은 크기가 맞지 않는, 즉 크기가 작은 돌의 개수이다.
다음 M개의 줄에는 크기가 작은 돌들의 번호가 주어진다. 1번 돌과 N번 돌은 충분히 크기가 크다고 가정한다.

출력
첫째 줄에 필요한 최소의 점프 횟수를 출력한다. 만약 N번 돌까지 점프해갈 수 없는 경우에는 -1을 출력한다.
"""
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

INF = float('inf')

rock_map = [True] * (n + 1)
max_jump = int((2 * n) ** 0.5) + 2
# dp[위치][마지막 점프 길이] 로 두어서 생각하자.
dp = [[INF] * (max_jump + 1) for _ in range(n + 1)]


for _ in range(m):
    idx = int(input().strip())
    rock_map[idx] = False

dp[1][0] = 0

# 최대 점프 가능 & 못 가는 위치 & 남은 거리 고려
for i in range(2, n+1):
    for j in range(1, max_jump+1):
        if not rock_map[i]:
            continue

        prev = i-j
        if prev < 1:
            break

        candidates = []

        for prev_jump in (j - 1, j, j + 1):
            # 범위 체크 & 도달 가능 체크
            if 0 <= prev_jump <= max_jump and dp[prev][prev_jump] != INF:
                # 가능하면 candidates에 추가
                candidates.append(dp[prev][prev_jump])
        if candidates:
            dp[i][j] = min(candidates) + 1

if min(dp[n]) == INF:
    print(-1)
    exit()

# print(dp)
print(min(dp[n]))


