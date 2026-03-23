# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력 1
1 2 4 3
1 2 3 4

예제 입력 2
5 5 3
5 4
5 2
1 2
3 4
3 1

예제 출력 2
3 1 2 5 4
3 1 4 2 5
"""
import sys
input = sys.stdin.readline
from collections import deque

# 정점, 간선, 탐색 시작
n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

dfs_visited = [False] * (n + 1)

# dfs
def dfs(dfs_graph, dfs_start):

    dfs_visited[dfs_start] = True
    print(dfs_start, end=" ")
    
    for next_node in dfs_graph[dfs_start]:
        if not dfs_visited[next_node]:
            dfs(dfs_graph, next_node)

# bfs
def bfs(bfs_graph, bfs_start):

    bfs_visited = [False] * (n + 1)
    queue = deque([bfs_start])

    while queue:
        v = queue.popleft()

        if not (bfs_visited[v]):
            print(v, end=" ")
            bfs_visited[v] = True

        for beside_node in bfs_graph[v]:
            if not bfs_visited[beside_node]:
                queue.append(beside_node)

dfs(graph, start)
print()
bfs(graph, start)