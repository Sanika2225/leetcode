class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute divisors
        factors = [[] for _ in range(n + 1)]

        for d in range(1, n):
            for length in range(d * 2, n + 1, d):
                factors[length].append(d)

        # Precompute substring costs
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = n

                for d in factors[length]:
                    changes = 0

                    for offset in range(d):
                        l = i + offset
                        r = j - d + 1 + offset

                        while l < r:
                            if s[l] != s[r]:
                                changes += 1

                            l += d
                            r -= d

                    best = min(best, changes)

                cost[i][j] = best

        # Suffix DP
        INF = 10**9
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for parts in range(1, k + 1):
                for j in range(i + 1, n):

                    dp[i][parts] = min(
                        dp[i][parts],
                        cost[i][j] + dp[j + 1][parts - 1]
                    )

        return dp[0][k]