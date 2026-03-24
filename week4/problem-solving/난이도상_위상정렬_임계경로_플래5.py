# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948
"""
모든 길은 로마로 통한다.

천 리 길도 한 걸음부터

월드 나라는 정말 특이하게도 각 도시를 연결하는 모든 도로가 일방통행이며, 
그 어떤 도시에서 출발해도 도로를 따라 출발한 도시로 돌아올 방법이 없다. 
월드 나라의 가장 유명한 두 도시는 한걸음과 로마다. 한걸음에서 출발하면 그 어떤 도시에도 갈 수 있고, 
그 어떤 도시에서 출발해도 로마에 도착할 수 있기 때문이다.

한걸음으로 들어오는 도로가 하나도 없고 로마에서 나갈 수 있는 도로 또한 하나도 없기 때문에 
당장 도로를 더 만들어야 할 것 같지만, 어떤 이유인지 월드 나라의 국왕 최백준은 
도로를 짓는 대신 월드 나라의 지도를 만들 것을 명하였다. 
이에 한걸음에서 출발해 로마에 도착하는 모든 경로를 전부 탐색하기 위해 선택받은 사람들이 한걸음에 모두 모였다.

어떻게 왔는지는 잘 모르겠지만, 아무튼 한걸음에 모인 사람들은 각자 로마에 이르는 서로 다른 경로를 하나씩 배정 받았다. 
모인 사람은 충분히 많아서 로마에 이르는 그 어떤 경로를 고르더라도 이를 배정 받은 사람이 있다. 
이들은 모두 동시에 한걸음에서 출발해서 쉬지 않고 로마까지 달린다.

이들이 모두 로마에 도착하는 데에 얼마의 시간이 걸리는가?

완성된 지도에 감격한 국왕 최백준은 이들의 업적을 치하하여 가장 오래 달린 사람들이 달린 도로에 전부 황금을 칠할 것을 명하였다. 
황금을 칠해야 할 도로의 수는 몇 개인가?

입력
첫째 줄에 월드 나라의 도시의 개수 
n(1 <= n <= 10,000)이 주어지고 둘째 줄에는 월드 나라의 도로의 개수 
m (
1 <= m <= 100,000)이 주어진다. 그리고 셋째 줄부터 
m+2번째 줄까지 도로의 정보를 나타내는 세 정수 
u, v, w가 공백으로 구분되어 주어진다. 이는 도시 
u에서 도시 
v로 향하는 일방통행 도로를 지나는데 
w의 시간이 걸림을 의미한다. 모든 도로는 
1 <= u <= 10,000, 
1 <= v <= 10,000, 
1 <= w <= 10,000을 만족한다. 
m+3번째 줄에는 한걸음과 로마의 도시 번호가 공백으로 구분되어 주어지며 두 도시 번호는 모두 
1 이상 
10,000 이하의 정수이다.

출력
첫째 줄에는 선택받은 사람들이 모두 로마에 도착하는 데 걸리는 시간을, 둘째 줄에는 황금을 칠해야 할 도로의 수를 출력한다.

예제 입력 1
7
9
1 2 4
1 3 2
1 4 3
2 6 3
2 7 5
3 5 1
4 6 4
5 6 2
6 7 5
1 7

예제 출력 1
12 # 모두 로마에 걸리는 시간
5 # 황금 칠 해야하는 도로의 수 ( 가장 오래 달린 사람들의 도로에 황금칠)
"""
import sys
input = sys.stdin.readline
from collections import deque

n = int(input().strip())
m = int(input().strip())

graph = [[] for x in range(n + 1)] # 이동 경로 그래프
indegree = [0] * (n + 1) # 차수
dist = [0] * (n + 1) # 가장 오래 걸리는 시간
parent = [[] for x in range(n + 1)] # 가장 오래 걸리는 시간 직전에 방문한 노드

for _ in range(m):
    start, destination, time_takes = map(int, input().split())
    graph[start].append((destination, time_takes))
    indegree[destination] += 1

han, rome = map(int, input().split())

# print("graph : ", graph)
# print("indegree : ", indegree)

queue = deque([han])

while queue:
    v = queue.popleft()

    for next_road in graph[v]:
        dest, times = next_road

        # 시간 걸릴 후보
        candidate = dist[v] + times

        if candidate > dist[dest]:
            dist[dest] = candidate
            parent[dest] = [v]

        elif candidate == dist[dest]:
            parent[dest].append(v)

        indegree[dest] -= 1

        if indegree[dest] == 0:
            queue.append(dest)

# print(parent)
print(dist[rome]) # 가장 오래 걸린 시간

# 다시 로마부터 역방향으로 카운트 하기
rome_queue = deque([rome])
visited = {rome}
count = 0

while rome_queue:
    current = rome_queue.popleft()

    for prev in parent[current]:
        count += 1
        if prev not in visited:
            visited.add(prev)
            rome_queue.append(prev)

# print(visited)
print(count)























