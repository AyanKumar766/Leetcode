class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Step 1: create a difference matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Step 2: apply each query using difference technique
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Step 3: prefix sum row-wise
        for r in range(n):
            for c in range(1, n):
                diff[r][c] += diff[r][c - 1]

        # Step 4: prefix sum column-wise
        for c in range(n):
            for r in range(1, n):
                diff[r][c] += diff[r - 1][c]

        # Step 5: extract n x n result
        result = [row[:n] for row in diff[:n]]
        return result
