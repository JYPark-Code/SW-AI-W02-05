# 스택 - 원 영역 (백준 플래4)
# 문제 링크: https://www.acmicpc.net/problem/10000
"""
x축 위에 원이 N개 있다. 원은 서로 교차하지 않는다. 하지만, 접할 수는 있다.

원으로 만들어지는 영역이 몇 개인지 구하는 프로그램을 작성하시오.

영역은 점의 집합으로 모든 두 점은 원을 교차하지 않는 연속되는 곡선으로 연결될 수 있어야 한다.



입력
첫째 줄에 원의 개수 N(1 ≤ N ≤ 300,000)이 주어진다.

다음 N개 줄에는 각 원의 정보 xi와 ri가 정수로 주어진다.
xi는 원의 중심 좌표이며, ri는 반지름이다. (-109 ≤ xi ≤ 109, 1 ≤ ri ≤ 109)

입력으로 주어지는 원은 항상 유일하다.

출력
첫째 줄에 원으로 인해서 만들어지는 영역의 개수를 출력한다.

예제 입력 1
2
1 3
5 1

예제 출력 1
3

예제 입력 2
3
2 2
1 1
3 1

예제 출력 2
5

예제 입력 3
4
7 5
-9 11
11 9
0 20

예제 출력 3
6
"""

"""
events 정렬
answer = 1   # 바깥 영역
stack = []

for event in events:
    if 시작점:
        stack.push(이 원 정보)
    else:  # 끝점
        현재 원 pop
        if 이 원이 L부터 R까지 다 채워졌으면:
            answer += 2
        else:
            answer += 1

        if 부모가 있으면:
            부모의 last 갱신
"""
import sys
input = sys.stdin.readline

N = int(input())

events = []
stack = []
answer = 1

for _ in range(N):
    x, r = map(int, input().split())
    L = x - r
    R = x + r
    events.append((L, 1, R)) # start
    events.append((R, 0, L)) # end

events.sort(key=lambda x: (x[0], x[1], -x[2]))

print(events)

# 좌표 시작,종점, 원의 끝점
for pos, type_ , other in events:

    # L, R, last
    if type_ == 1:
        stack.append([pos, other, pos])

    if type_ == 0:
        L, R, last = stack.pop()

        if last == R:
            answer += 2
        else:
            answer += 1

        if stack and stack[-1][2] == L:
            stack[-1][2] = R

print(answer)







