class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        north = [math.inf] * (n + 1)
        south = [0] * (n + 1)
        west = [math.inf] * (n + 1)
        east = [0] * (n + 1)

        for x, y in buildings:
            north[x] = min(north[x], y)
            south[x] = max(south[x], y)
            west[y] = min(west[y], x)
            east[y] = max(east[y], x)

        return sum(
            north[x] < y < south[x]
            and west[y] < x < east[y]
            for x, y in buildings
        )
