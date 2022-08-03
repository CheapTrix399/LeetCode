# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = ListNode()
        carry = 0
        temp = ans
        while((l1!=None)|(l2!=None)):
            if(l1==None):
                sum_node = l2.val + carry
                l2=l2.next
            elif(l2==None):
                sum_node = l1.val + carry
                l1=l1.next
            else:
                sum_node = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            carry = int(sum_node/10)
            temp.val = sum_node%10
            if((l1!=None)|(l2!=None)):
                temp.next = ListNode()
            else:
                if(carry>0):
                    temp.next = ListNode(val=carry)
            temp = temp.next
        return ans