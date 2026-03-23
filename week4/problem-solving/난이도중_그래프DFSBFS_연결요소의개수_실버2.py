# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1
6 5
1 2
2 5
5 1
3 4
4 6

예제 출력 1
2

예제 입력 2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

예제 출력 2
1

"""
import sys
input = sys.stdin.readline
from collections import deque

# n : 정점 개수, m : 간선 개수
n , m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = set()

count = 0

# 그래프 채우기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def bfs(graph_, start):
    queue = deque([start])
    bfs_visited = set()

    while queue:
        v = queue.popleft()

        for i in graph_[v]:
            if i not in bfs_visited:
                queue.append(i)
                bfs_visited.add(i)

    return bfs_visited

for i in range(1, n + 1):

    if i in visited:
        continue

    visited_set = bfs(graph, i)
    visited.update(visited_set)
    count += 1

    if len(visited_set) == n:
        break

print(count)