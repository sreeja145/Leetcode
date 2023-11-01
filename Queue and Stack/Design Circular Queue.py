"""
Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q=[]
        self.k=k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.q)>=self.k:
            return False
        self.q.append(value)
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if len(self.q)==0:
            return False
        self.q=self.q[1:]
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if len(self.q)==0:
            return -1
        return self.q[0]
        

    def Rear(self):
        """
        :rtype: int
        """
        if len(self.q)==0:
            return -1
        return self.q[-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.q)==0:
            return True
        return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.q)==self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
