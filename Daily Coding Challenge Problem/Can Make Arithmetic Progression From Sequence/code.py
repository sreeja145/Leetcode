def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        real_diff=arr[1]-arr[0]
        n=len(arr)
        for i in range(1,n-1):
            diff=arr[i+1]-arr[i]
            if real_diff!=diff:
                return False
        return True
