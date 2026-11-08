# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        p=head
        arr=list()
        while p:
            arr.append(p.val)
            p=p.next
        c=len(arr)
        max_s=0
        for i in range(c//2):
            max_s=max(max_s, arr[i]+arr[c-i-1])
        return max_s

        