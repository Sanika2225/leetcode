
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0

        def push(node, l, r):
            if lazy[node]:
                d = lazy[node]
                left = node * 2
                right = left + 1

                mid = (l + r) // 2
                len_left = mid - l + 1
                len_right = r - mid

                for child, length in (
                    (left, len_left),
                    (right, len_right)
                ):
                    old_sum = tree[child]
                    sq[child] = (
                        sq[child] + 2 * d * old_sum
                        + d * d * length
                    ) % MOD
                    tree[child] = (
                        old_sum + d * length
                    ) % MOD
                    lazy[child] += d

                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                d = 1
                length = r - l + 1
                old_sum = tree[node]

                sq[node] = (
                    sq[node] + 2 * old_sum
                    + length
                ) % MOD
                tree[node] = (old_sum + length) % MOD
                lazy[node] += 1
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            tree[node] = (
                tree[node * 2] + tree[node * 2 + 1]
            ) % MOD
            sq[node] = (
                sq[node * 2] + sq[node * 2 + 1]
            ) % MOD

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            # Add 1 to distinct counts of subarrays
            # whose starting index is in [prev + 1, i].
            update(1, 0, n - 1, prev + 1, i)

            # Sum of squares for all subarrays ending at i.
            ans = (ans + sq[1]) % MOD
            last[x] = i

        return ans
