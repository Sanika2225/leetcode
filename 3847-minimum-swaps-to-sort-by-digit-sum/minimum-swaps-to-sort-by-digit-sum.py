class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        # Sort by digit sum, then by number
        arr = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

        # Map each number to its correct sorted index
        pos = {num: i for i, num in enumerate(arr)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue
            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += max(0, cycle_size - 1)

        return swaps
        