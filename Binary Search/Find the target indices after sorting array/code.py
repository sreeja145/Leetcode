def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices=[]
        nums.sort()
        first_pos=-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                first_pos=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        
        
        low=0
        high=len(nums)-1
        last_pos=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                last_pos=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        if last_pos==first_pos and last_pos!=-1:
            indices.append(first_pos)
            return indices
        if last_pos!=-1 and first_pos!=last_pos and first_pos!=-1:
            # indices.append(last_pos)
            for i in range(first_pos,last_pos+1):
                indices.append(i)
        
        return indices
