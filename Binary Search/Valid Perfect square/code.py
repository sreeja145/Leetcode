def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low=0
        high=num
        while low<=high:
            mid=(low+high)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                high=mid-1
            else:
                low=mid+1
        return False
