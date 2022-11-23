#Time Complexity:: O(nlogk) - using a heap to sort the k numbers in the heap at a time
#Space Complexity:: O(k)- the size of the heap is restricted to k
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hq = [] #an array that will be used as a heap
        
        for num in nums: #for loop to traverse every number
            heappush(hq,num) #creating a heap using heap and pushing all the numbers into it
            if len(hq)>k: #when the heap length is greater than k pop elements from the top which are smaller since min heap
                heappop(hq) 
                
        return hq[0] #return the top of the min heap(correct syntax for heap)
                