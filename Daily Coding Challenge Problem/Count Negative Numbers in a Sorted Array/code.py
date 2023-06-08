def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        columns=len(grid[0])
        negatives=0
        for i in range(rows):
            low=0
            high=columns-1
            if grid[i][0]<0:
                negatives+=columns
            elif grid[i][-1]>0:
                negatives+=0
            else:
                while low<=high:
                    mid=(low+high)//2
                    if grid[i][mid]>=0:
                        low=mid+1
                    elif grid[i][mid]<0:
                        high=mid-1
                negatives+=columns-low
        return negatives
