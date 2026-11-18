class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        islands = 0

        def dfs(row, col):
            grid[row][col] = '0'

            for direction in directions:
                dx, dy = direction
                if 0 <= (row + dx) < rows and 0 <= (col + dy) < cols and grid[row+dx][col+dy] == '1':
                    dfs(row+dx,col+dy)
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands+=1
                    dfs(row, col)
        
        return islands