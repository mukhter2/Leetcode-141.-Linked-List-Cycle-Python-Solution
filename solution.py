# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pdict = {}
        if head==None:
            return False
        while head.next is not None:
            
            x=head.val
            if pdict.get(head) is None:
                pdict[head]=1
            else:
                pdict[head]+=1
            if pdict[head]>1:
                return True
            head=head.next
        return False
