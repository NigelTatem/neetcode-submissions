class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        check_directions = [(0,1), (1,0), (-1,0), (0,-1)]
        count = 0

        def dfs(pos):
            row, col = pos
            grid[row][col] = '0'

            for direction in check_directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                # 3. Check if the cell is land ('1')
                    if grid[new_row][new_col] == '1':
                        dfs((new_row, new_col))

        for i, row in enumerate(grid):
            for j, column in enumerate(row):
                if column == '1':
                    dfs((i, j))
                    count += 1
        
        return count
                
