class Solution:
    def getTotalIsles(self, island_map: list[list[str]]) -> int:
        
        def explore_land(x, y):
            if x < 0 or y < 0 or x >= len(island_map) or y >= len(island_map[0]) or island_map[x][y] != 'L':
                return
            island_map[x][y] = 'W'
            explore_land(x + 1, y)
            explore_land(x - 1, y)
            explore_land(x, y + 1)
            explore_land(x, y - 1)

        if not island_map:
            return 0
        
        island_count = 0

        for row in range(len(island_map)):
            for col in range(len(island_map[0])):
                if island_map[row][col] == 'L':
                    explore_land(row, col)
                    island_count += 1
        
        return island_count
