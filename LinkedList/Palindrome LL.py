"""
iven the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        is_break=0
        if head is None and head.next is None:
            return True
        
        
        prev=head
        final=head.next
        
        while final!=None and final.next!=None:
            if final==final.next:
                is_break=1
                break
            final=final.next
        
        '''if is_break ==0:
            return False '''
        
        while final.next!=None and final!=None:
            if prev.next!=final.next:
                return False
            final=final.next
            
        return True
        
