
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 31

        # Step 1: Count set bits at each position
        for num in nums:
            for i in range(31):
                if num & (1 << i):
                    bits[i] += 1

        ans = 0

        # Step 2: Construct k maximum numbers
        for _ in range(k):
            num = 0

            for i in range(31):
                if bits[i] > 0:
                    num |= (1 << i)
                    bits[i] -= 1

            # Step 3: Add square modulo MOD
            ans = (ans + num * num) % MOD

        return ans
