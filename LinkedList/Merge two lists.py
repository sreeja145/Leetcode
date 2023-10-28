"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return list1
        
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        if list1.val<list2.val:
            new_head=list1
            list1=list1.next
        else:
            new_head=list2
            list2=list2.next
            
        last_node=new_head
        
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                last_node.next=list1
                last_node=list1
                list1=list1.next
            else:
                last_node.next=list2
                last_node=list2
                list2=list2.next
                
        if list1==None:
            last_node.next=list2
        if list2==None:
            last_node.next=list1
       
        return new_head
