def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        rows=0
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            sum=mid*(mid+1)//2
            if sum<=n:
                low=mid+1
            else:
                high=mid-1
        return high
