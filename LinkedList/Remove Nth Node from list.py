"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count=0
        head_=head
        head_copy=head
        while head_!=None:
            count+=1
            head_=head_.next
        if count==1:
            return None
        if count==n:
            head=head.next
            return head
        for i in range(count-n-1):
            head_copy=head_copy.next
        temp=head_copy.next
        head_copy.next=head_copy.next.next
        del temp
        return head
