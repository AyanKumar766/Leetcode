def magic(grid, istart, iend, jstart, jend):

    num = [0] * 9
    target_sum = -1

    # Check rows
    for i in range(istart, iend + 1):
        row_sum = 0
        for j in range(jstart, jend + 1):
            row_sum += grid[i][j]

        if target_sum == -1:
            target_sum = row_sum
        elif row_sum != target_sum:
            return 0

    # Check columns and count numbers
    total_sum = 0
    for j in range(jstart, jend + 1):
        col_sum = 0
        for i in range(istart, iend + 1):
            val = grid[i][j]

            if val < 1 or val > 9:
                return 0

            num[val - 1] += 1
            col_sum += val
            total_sum += val

        if col_sum != target_sum:
            return 0

    # Check diagonals
    i = istart
    j = jstart

    diag1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
    diag2 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]

    if diag1 != target_sum or diag2 != target_sum:
        return 0

    if total_sum == 45 and num == [1] * 9:
        return 1

    return 0


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        total = 0
        for istart in range(len(grid) - 2):
            for jstart in range(len(grid[0]) - 2):
                total += magic(grid, istart, istart + 2, jstart, jstart + 2)

        return total