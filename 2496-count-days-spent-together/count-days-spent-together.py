
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def dayOfYear(date):
            month, day = map(int, date.split('-'))
            return sum(months[:month - 1]) + day

        a1 = dayOfYear(arriveAlice)
        a2 = dayOfYear(leaveAlice)
        b1 = dayOfYear(arriveBob)
        b2 = dayOfYear(leaveBob)

        start = max(a1, b1)
        end = min(a2, b2)

        return max(0, end - start + 1)
