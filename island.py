x = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
def island(grid):
    rows = len(grid)
    cols = len(grid[0])
    def dfs(r,c):
        if r < 0 or r > rows-1 or c < 0 or c > cols-1:
            return 0
        if grid[r][c] == "1":
            grid[r][c] = "0"
        else:
            return
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r+1,c)
        dfs(r,c-1)
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r,c)
    return count
print(island(x))