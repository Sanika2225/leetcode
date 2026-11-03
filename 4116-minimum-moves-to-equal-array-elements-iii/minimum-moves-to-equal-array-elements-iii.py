class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        total = sum(nums)

        return maxi * len(nums) - total