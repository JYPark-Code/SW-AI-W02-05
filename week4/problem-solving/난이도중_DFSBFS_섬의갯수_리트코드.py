# 링크 : https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150
# 3일차 코어타임 문제
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.bfs(grid, i, j, len(grid), len(grid[0]))
        return count

    def bfs(self, graph, x, y, n, m):
        visited = set()
        queue = deque([(x, y)])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while queue:
            vx, vy = queue.popleft()

            for i in range(4):
                nx = vx + dx[i]
                ny = vy + dy[i]

                # 범위 내에 있을 때만 계산
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == "1":
                        graph[nx][ny] = 0
                        queue.append((nx, ny))