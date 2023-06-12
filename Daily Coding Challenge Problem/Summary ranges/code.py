def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n=len(nums)
        i=0
        lstr=[]
        while i<n:
            start=nums[i]
            while i<n-1 and nums[i]==nums[i+1]-1:
                i+=1
            end=nums[i]
            if start==end:
                lstr.append(str(start))
            else:
                lstr.append(str(start)+"->"+str(end))
            i=i+1
        return lstr
