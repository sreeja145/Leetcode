class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=m-1,n-1
        w=len(nums1)-1
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[w]=nums2[j]
                w=w-1
                j=j-1
            elif nums1[i]>nums2[j]:
                nums1[w]=nums1[i]
                w=w-1
                i=i-1
            else:
                nums1[w]=nums1[i]
                nums1[w-1]=nums2[j]
                i=i-1
                j=j-1
                w=w-2
        while j>=0:
            nums1[w]=nums2[j]
            j=j-1
            w=w-1
