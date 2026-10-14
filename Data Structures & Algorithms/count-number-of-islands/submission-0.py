class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        count = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] != "1":
                    continue
                count += 1 # new island found
                stack = [(r,c)]
                grid[r][c] = "0" # sink
                while stack:# if stack is not empty!!
                    cr, cc = stack.pop() # empty stack
                    for dr, dc in DIRS:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            stack.append((nr, nc))

        return count






        