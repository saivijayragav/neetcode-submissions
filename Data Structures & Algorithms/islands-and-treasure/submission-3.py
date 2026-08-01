class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        dire = [(0, 1),(1, 0), (-1, 0), (0, -1)]
        while q:
            i, j, d = q.popleft()
            for x, y in dire:
                di, dj = i+x, j+y
                if 0<=di<m and 0<=dj<n and grid[di][dj] > d:
                    grid[di][dj] = d+1
                    q.append((di, dj, d+1))
        