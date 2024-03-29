class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
    
class MyLinkedList(object):
  def __init__(self):
        self.head=None
        self.size=0
        

  def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>self.size:
            return -1
        if self.size==0:
            return -1
        if index==0:
            return self.head.val
        else:
            current=self.head
            count=0
            while current!=None:
                if index==count:
                    return current.val
                count=count+1
                current=current.next
            return -1
    
                
        
        

def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode=ListNode(val)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.size+=1
def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.size==0:
            self.addAtHead(val)
        else:
            newNode=ListNode(val)
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=newNode
            self.size+=1

def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.size==0 and index>0:
            return -1
        if index==0:
            self.addAtHead(val)
        if index==self.size:
            self.addAtTail(val)
        
        else:
            count=0
            current=self.head
            prev=None
            newNode=ListNode(val)
            while count!=index and current.next!=None:
                if not current:
                    return
                count=count+1
                prev=current
                current=current.next
            if count==index:
                if prev:
                    prev.next=newNode
                    newNode.next=current
                    self.size+=1
def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index==0:
            ans=self.head.val
            newHead=self.head.next
            self.head=newHead
            self.size-=1
            return ans
        else:
            count=0
            current=self.head
            prev=None
            while count!=index and current.next!=None:
                prev=current
                current=current.next
                count+=1
            if count==index:
                prev.next=current.next
                self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
