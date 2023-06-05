def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s=set()
        arr=[]
        for i in nums1:
            if i not in s:
                s.add(i)
        for i in nums2:
            if i in s:
                arr.append(i)
        s1=set()
        for i in arr:
            s1.add(i)
        

        return s1
