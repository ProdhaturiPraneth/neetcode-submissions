# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        if head is None:
            return None
        while head!=None:
            arr.append(head.val)
            head=head.next
        n=len(arr)
        for i in range(0,n//2):
            arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        head=ListNode(arr[0])
        current=head
        for value in arr[1:]:
            current.next=ListNode(value)
            current=current.next
        return head