# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
"""
연세대학교가 위치한 신촌역이 속한 2호선은 그림과 같이
N개의 역이 원형으로 연결되어 있다. 각 역은 고유 번호가 할당돼 있으며 역들의 고유 번호는 서로 다르다. 그리고 특정 역의 다음 역은 시계 방향으로 인접한 역을 의미하고, 이전 역은 반시계 방향으로 인접한 역을 의미한다.

2호선은 지하철 노선들 중 유일한 흑자 노선이다. 때문에 2호선 공사 자금이 넉넉하기에
M번의 공사를 거치려고 한다. 각 공사는 다음 4가지 중 하나를 시행한다.

고유 번호
i를 가진 역의 다음 역의 고유 번호를 출력하고, 그 사이에 고유 번호
j인 역을 설립한다.
고유 번호
i를 가진 역의 이전 역의 고유 번호를 출력하고, 그 사이에 고유 번호
j인 역을 설립한다.
고유 번호
i를 가진 역의 다음 역을 폐쇄하고 그 역의 고유 번호를 출력한다.
고유 번호
i를 가진 역의 이전 역을 폐쇄하고 그 역의 고유 번호를 출력한다.
이 때, 이미 설립한 역은 다시 설립하지 않으며 폐쇄한 역은 다시 설립될 수 있다. 그리고 폐쇄 작업은 현재 설립된 역이
2개 이상일 때만 들어온다.

2호선을 공사하는 프로그램을 만들어보자.

입력
첫 번째 줄에 공사를 시작하기 이전에 있는 역의 개수를 나타내는 양의 정수
N과 공사 횟수를 나타내는 양의 정수
M이 주어진다. (
1 <= N <= 500,000,
1 <= M <= 1,500,000)

두 번째 줄에는 공사를 시작하기 이전에 있는 역의 고유 번호를 시계 방향 순서대로 주어진다. 같은 고유 번호를 가진 역은 주어지지 않는다.

이후
M개의 줄에 걸쳐서 공사에 대한 정보를 다음과 같이 주어진다.

BN
i j : 고유 번호
i를 가진 역의 다음 역의 고유 번호를 출력하고, 그 사이에 고유 번호
j인 역을 설립한다.
BP
i j : 고유 번호
i를 가진 역의 이전 역의 고유 번호를 출력하고, 그 사이에 고유 번호
j인 역을 설립한다.
CN i : 고유 번호
i를 가진 역의 다음 역을 폐쇄하고 그 역의 고유 번호를 출력한다.
CP i : 고유 번호
i를 가진 역의 이전 역을 폐쇄하고 그 역의 고유 번호를 출력한다.
입력으로 들어오는 모든 역의 고유 번호는
1 이상
1,000,000 이하의 양의 정수다. 폐쇄 작업은 현재 설립된 역이
2개 이상일 때만 들어오며, 이미 설립된 역은 또 설립될 수 없지만 폐쇄된 역은 다시 설립될 수 있다.

출력
각 공사에 대한 출력 값을
M개의 줄에 걸쳐서 출력한다.

입력 1
4 4
2 7 3 5
BN 5 11
BP 3 6
CP 2
CN 7

출력 1
2
7
11
6
"""
# import sys
# input = sys.stdin.readline

# total_station, total_construction = map(int, input().split())
# map_info = list(map(int, input().split())) # 2 7 3 5
#
# # print(total_station, total_station)
# # print(map_info)
#
# station = {}
# answer = []
#
# # key = prev,next -> 지금 역 : 이전 역, 다음 역
# for idx, i in enumerate(map_info):
#     station[i] = [map_info[(idx-1) % len(map_info)], map_info[(idx+1) % len(map_info)]]
#
# for _ in range(total_construction):
#     construction = input().strip().split()
#
#     if len(construction) == 3:
#         cmd, selected, target  = construction
#         selected = int(selected)
#         target = int(target)
#
#         if cmd == "BN":
#             # 다음 역
#             next_station = station[selected][1]
#             station[selected][1] = target
#             station[target] = [selected, next_station]
#             station[next_station][0] = target
#             answer.append(str(next_station))
#
#         # print(cmd, selected, target)
#
#         elif cmd == "BP":
#             # 이전 역
#             prev_station = station[selected][0]
#             station[selected][0] = target
#             station[target] = [prev_station, selected]
#             station[prev_station][1] = target
#             answer.append(str(prev_station))
#
#     elif len(construction) == 2:
#         cmd, selected = construction
#         selected = int(selected)
#
#         if cmd == "CN":
#             # 다음 역
#             next_station = station[selected][1]
#             answer.append(str(next_station))
#             next_next_station = station[next_station][1]
#             station[selected][1] = next_next_station
#             station[next_next_station][0] = selected
#             del station[next_station]
#
#         elif cmd == "CP":
#             # 이전 역
#             prev_station = station[selected][0]
#             answer.append(str(prev_station))
#             prev_prev_station = station[prev_station][0]
#             station[selected][0] = prev_prev_station
#             station[prev_prev_station][1] = selected
#             del station[prev_station]
#
# sys.stdout.write("\n".join(answer))

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stations = list(map(int, input().split()))

MAX = 1000001

prev = [0] * MAX
next = [0] * MAX

# 초기 원형 연결
for i in range(N):
    prev[stations[i]] = stations[(i-1) % N]
    next[stations[i]] = stations[(i+1) % N]

answer = []

for _ in range(M):
    cmd = input().split()

    if cmd[0] == "BN":
        i = int(cmd[1])
        j = int(cmd[2])

        nxt = next[i]
        answer.append(str(nxt))

        next[i] = j
        prev[j] = i
        next[j] = nxt
        prev[nxt] = j

    elif cmd[0] == "BP":
        i = int(cmd[1])
        j = int(cmd[2])

        prv = prev[i]
        answer.append(str(prv))

        prev[i] = j
        next[j] = i
        prev[j] = prv
        next[prv] = j

    elif cmd[0] == "CN":
        i = int(cmd[1])

        target = next[i]
        answer.append(str(target))

        nn = next[target]
        next[i] = nn
        prev[nn] = i

    elif cmd[0] == "CP":
        i = int(cmd[1])

        target = prev[i]
        answer.append(str(target))

        pp = prev[target]
        prev[i] = pp
        next[pp] = i

sys.stdout.write("\n".join(answer))