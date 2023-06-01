def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count=len(arr1)
        arr2.sort()
        
        for num in arr1:
            low=0
            high=len(arr2)-1
            while low<=high:
                mid=(low+high)//2
                if abs(arr2[mid]-num)<=d:
                    count-=1
                    break
                elif arr2[mid]>num:
                    high=mid-1
                else:
                    low=mid+1


        return count
