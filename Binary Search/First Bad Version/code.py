def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=0
        right=n+1
        ans=n
        while left<=right:
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid-1
                ans=mid
            else:
                left=mid+1
        return ans
