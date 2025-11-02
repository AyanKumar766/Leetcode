class Solution:
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0]*n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 2
        for r, c in walls:
            grid[r][c] = 2
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        for gr, gc in guards:
            for dr, dc in dirs:
                x, y = gr + dr, gc + dc
                while 0 <= x < m and 0 <= y < n and grid[x][y] < 2:
                    grid[x][y] = 1
                    x += dr
                    y += dc
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
        return res
