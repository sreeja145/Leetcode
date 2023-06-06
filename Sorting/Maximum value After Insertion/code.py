def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        def minimize(num,x):
            for i,d in enumerate(num):
                if x<d:
                    return num[:i]+x+num[i:]
            return num+x
        def maximize(num,x):
            for i,d in enumerate(num):
                if x>d:
                    return num[:i]+x+num[i:]
            return num+x
        x=str(x)
        if n[0]=='-':
            return '-'+minimize(n[1:],x)
        return maximize(n,x)
