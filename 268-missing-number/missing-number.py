class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = sum(range(len(nums)+1))
        return sum2 - sum1
        