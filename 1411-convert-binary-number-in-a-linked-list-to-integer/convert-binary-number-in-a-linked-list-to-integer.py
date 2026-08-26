# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        temp = head

        while temp:
            num = num * 2 + temp.val
            temp = temp.next

        return num
        