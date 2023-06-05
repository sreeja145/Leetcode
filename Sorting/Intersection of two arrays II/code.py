def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        arr=[]
        n1=0
        n2=0

        while n1<len(nums1) and n2<len(nums2):
            if nums1[n1]<nums2[n2]:
                n1+=1
            elif nums2[n2]<nums1[n1]:
                n2+=1
            else:
                arr.append(nums1[n1])
                n1+=1
                n2+=1
        return arr
