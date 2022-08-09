# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        if(head == None):
            return None
        while(head.val == val):
            head = head.next
            if(head == None):
                return None
        prev = head
        if(prev == None):
            return None
        pointer = prev.next
        while(pointer != None):
            if(pointer.val == val):
                while(pointer.val == val):
                    pointer = pointer.next
                    if(pointer == None):
                        break
            prev.next = pointer
            prev = pointer
            if(pointer != None):
                pointer = pointer.next
        return head