class Solution:
    def countIslands(self, map_grid: list[list[str]]) -> int:

        def explore(x, y):
            if x < 0 or y < 0 or x >= len(map_grid) or y >= len(map_grid[0]) or map_grid[x][y] != 'L':
                return
            map_grid[x][y] = 'W'
            explore(x + 1, y)
            explore(x - 1, y)
            explore(x, y + 1)
            explore(x, y - 1)

        if not map_grid:
            return 0

        island_count = 0

        for row in range(len(map_grid)):
            for col in range(len(map_grid[0])):
                if map_grid[row][col] == 'L':
                    explore(row, col)
                    island_count += 1

        return island_count
