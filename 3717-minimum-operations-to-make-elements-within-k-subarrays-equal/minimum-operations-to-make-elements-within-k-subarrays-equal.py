
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        size = len(vals)
        pos = {v: i for i, v in enumerate(vals)}

        cnt = [0] * (size + 1)
        sm = [0] * (size + 1)
        total = 0

        def update(bit, i, delta):
            i += 1
            while i <= size:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def kth(k):
            idx = 0
            bit = 1 << (size.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= size and cnt[nxt] < k:
                    idx = nxt
                    k -= cnt[nxt]
                bit >>= 1

            return idx

        costs = []

        # Calculate cost of every window of size x
        for i, v in enumerate(nums):
            p = pos[v]

            update(cnt, p, 1)
            update(sm, p, v)
            total += v

            if i >= x:
                old = nums[i - x]
                q = pos[old]

                update(cnt, q, -1)
                update(sm, q, -old)
                total -= old

            if i >= x - 1:
                mid = kth((x + 1) // 2)
                median = vals[mid]

                left_count = query(cnt, mid + 1)
                left_sum = query(sm, mid + 1)

                right_count = x - left_count
                right_sum = total - left_sum

                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

                costs.append(cost)

        # DP over original array indices
        INF = 10**30
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(n - 1, -1, -1):
                curr[i] = curr[i + 1]

                if i < len(costs):
                    curr[i] = min(
                        curr[i],
                        costs[i] + prev[i + x]
                    )

            prev = curr

        return prev[0]
