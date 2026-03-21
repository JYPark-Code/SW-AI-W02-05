# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
"""
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
"""
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

parent = [0] * (T+1)
graph = [[] for _ in range(T+1)]
parent[1] = 1

for _ in range(T-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 풀이

def dfs(node):
    for next_node in graph[node]:
        if parent[next_node] == 0:
            parent[next_node] = node
            dfs(next_node)


dfs(1)
print(*parent[2:], sep="\n")

# BFS 풀이
def bfs(start):
    queue = deque([start])
    parent[start] = start  # 루트 방문 처리

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if parent[next_node] == 0:
                parent[next_node] = node
                queue.append(next_node)

bfs(1)
print(*parent[2:], sep="\n")