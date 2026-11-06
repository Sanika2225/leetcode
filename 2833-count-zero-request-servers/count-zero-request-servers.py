from typing import List
from collections import Counter

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda a: a[1])

        q = sorted((t, i) for i, t in enumerate(queries))

        freq = Counter()
        ans = [0] * len(queries)

        left = right = 0

        for t, idx in q:

            while right < len(logs) and logs[right][1] <= t:
                freq[logs[right][0]] += 1
                right += 1

            while left < right and logs[left][1] < t - x:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            ans[idx] = n - len(freq)

        return ans