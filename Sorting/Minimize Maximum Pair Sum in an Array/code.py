def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return nums
        import sys
        
        nums.sort()
        low=0
        high=len(nums)-1
        max=0

        while low<high:
            
            if nums[low]+nums[high]>max:
                max=nums[low]+nums[high]
                
            low=low+1
            high=high-1
        return max
