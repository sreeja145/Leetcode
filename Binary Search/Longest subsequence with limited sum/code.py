def answerQueries(self, nums, queries):
        def bin_search(nums,target):
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    return mid+1
                elif nums[mid]>target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return len(nums) if ans==-1 else ans

        answer=[]
        n,m=len(nums),len(queries)
        nums.sort()
        for i in range(1,n):
            nums[i]=nums[i]+nums[i-1]
        for j in range(m):
            target=queries[j]
            answer.append(bin_search(nums,target))
        return answer
