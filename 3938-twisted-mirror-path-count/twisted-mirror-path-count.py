class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # One initial path at the starting cell
        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):

                right = dp[i][j][0]
                down = dp[i][j][1]

                if grid[i][j] == 0:
                    total = (right + down) % MOD

                    # Move right
                    if j + 1 < n:
                        dp[i][j + 1][0] = (
                            dp[i][j + 1][0] + total
                        ) % MOD

                    # Move down
                    if i + 1 < m:
                        dp[i + 1][j][1] = (
                            dp[i + 1][j][1] + total
                        ) % MOD

                else:
                    # Mirror: right -> down
                    if i + 1 < m:
                        dp[i + 1][j][1] = (
                            dp[i + 1][j][1] + right
                        ) % MOD

                    # Mirror: down -> right
                    if j + 1 < n:
                        dp[i][j + 1][0] = (
                            dp[i][j + 1][0] + down
                        ) % MOD

        return sum(dp[m - 1][n - 1]) % MOD