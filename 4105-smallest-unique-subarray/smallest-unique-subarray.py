
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def check(length):
            base1, mod1 = 100019, 10**9 + 7
            base2, mod2 = 100043, 10**9 + 9

            power1 = pow(base1, length - 1, mod1)
            power2 = pow(base2, length - 1, mod2)

            h1 = h2 = 0
            freq = {}

            # Calculate hash of first window
            for i in range(length):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2

            freq[(h1, h2)] = 1

            # Slide the window
            for i in range(length, n):
                h1 = ((h1 - nums[i-length] * power1) * base1
                      + nums[i]) % mod1

                h2 = ((h2 - nums[i-length] * power2) * base2
                      + nums[i]) % mod2

                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return 1 in freq.values()

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
