def sortColors(self,A):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(A)):
            value = A[i]
            j = i
            while j > 0 and A[j - 1] > value:
                A[j] = A[j - 1]
                j = j - 1

            A[j] = value
