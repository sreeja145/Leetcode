def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start,end=0,0
        while end<len(nums) and start<=end:
            if nums[start]!=0:
                start=start+1
                end=end+1
            else:
                if nums[end]!=0:
                    nums[start]=nums[end]
                    nums[end]=0
                else:
                    end=end+1
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
