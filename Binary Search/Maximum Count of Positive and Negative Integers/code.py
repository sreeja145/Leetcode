def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # corner case 1
        if nums[0] > 0 or nums[-1]<0: 
            return n

        # corner case 2
        if nums[0]==nums[-1] and nums[0] == 0:
            return 0
        
        # try to find the index of -0.5
        left, right =0, n
        while left < right:
            mid = (left+right)//2
            if nums[mid] < -0.5:
                left = mid + 1
            else: 
                right = mid

        n_neg = left

        # try to find the index of 0.5
        left, right = 0, n
        while left < right:
            mid = (left+right+1)//2
            if nums[mid] > 0.5:
                right = mid - 1
            else: 
                left = mid
        
        n_pos = n - right - 1

        return max(n_pos, n_neg)
