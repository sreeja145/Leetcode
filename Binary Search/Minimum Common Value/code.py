def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def binarysearch(nums,x):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==x:
                    return True
                elif nums[mid]>x:
                    right=mid-1
                else:
                    left=mid+1
            return False
        for i in nums1:
            if binarysearch(nums2,i):
                return i 
        return -1
