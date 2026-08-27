class Solution:
    def findComplement(self, num: int) -> int:
        temp = 1

        while temp <= num:
            temp = temp << 1

        temp = temp - 1

        return num ^ temp