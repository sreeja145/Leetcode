def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 :
            return t
        if len(t)==0:
            return s
        freq=[0]*26
        n=len(s)
        m=len(t)
        for i in range(n):
            freq[ord(s[i])-ord('a')]+=1
        for i in range(m):
            freq[ord(t[i])-ord('a')]-=1
            if freq[ord(t[i])-ord('a')]==-1:
                return t[i] 
