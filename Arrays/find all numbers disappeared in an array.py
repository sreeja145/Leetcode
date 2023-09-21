def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            a=abs(n)-1
            if nums[a]>0 and nums[a]<=(len(nums)-1):
                nums[a]=nums[a]*-1
        return [i+1 for i in range(len(nums)) if nums[i]>0]
  """
  Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""
