class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0

        def dfs(r ,c):
            if (r >= rows or r < 0
                or c >= cols or c < 0
                or (r, c) in visit or grid[r][c] == "0"):
                return
            visit.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if (r,c) in visit:
                    continue
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands