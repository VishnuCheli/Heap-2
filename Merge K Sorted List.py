#Time Complexity:: O(nlogk) - using a minheap to sort the k nodes in the heap at a time
#Space Complexity:: O(k)- the size of the heap can be at most k
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #custom comparator(important)-overloading less than function
        ListNode.__lt__ = lambda a,b: a.val < b.val #creating a listnode function-comparing a.val and b.val, where a goes to the top if true otherwise b is on top
        minheap = [] #creating a minheap as an array
        
        result = ListNode(-1) #creating a dummy node and assigning it to result
        
        curr = result #creating a temperory node to use for traversal
        
        for lhead in lists: #traversing each element in the list and adding to minheap
            if lhead: #if lhead is not null(ex empty linked list)
                heappush(minheap,lhead) #pushing the node into the minheap
        
        while minheap: #minheap isn't empty
            top = heappop(minheap) #top node of the minheap
            curr.next = top #current.next is assigned the popped node which adds to the merged linked list
            curr = curr.next #current pointer is moved
            if top.next: #if there's a node after the newly added element 
                heappush(minheap,top.next)#then add that node to the minheap
        
        return result.next #return the main head nodes next node as the result linked list head