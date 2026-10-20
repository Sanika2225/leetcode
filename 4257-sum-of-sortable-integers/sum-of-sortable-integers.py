
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        qelvarodin = nums

        # Prefix maximum
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        # Suffix minimum
        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # Count adjacent descents
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = (
                pref_drop[i - 1] + (nums[i - 1] > nums[i])
            )

        def check(k: int) -> bool:
            for start in range(0, n, k):
                end = start + k - 1

                # Descents inside the block
                drops = pref_drop[end] - pref_drop[start]

                # Include the circular edge
                if nums[end] > nums[start]:
                    drops += 1

                # A block must be cyclically sortable
                if drops > 1:
                    return False

                # Previous blocks must not exceed future blocks
                if pref_max[start] > suff_min[start]:
                    return False

            return True

        ans = 0

        # Enumerate divisors of n
        i = 1
        while i * i <= n:
            if n % i == 0:
                if check(i):
                    ans += i

                other = n // i
                if other != i and check(other):
                    ans += other

            i += 1

        return ans
