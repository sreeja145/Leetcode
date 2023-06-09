def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        chars=letters[0]
        start=0
        end=len(letters)-1
        while start<=end:
            mid=(start+end)//2
            if ord(letters[mid])-ord('a')>ord(target)-ord('a'):
                chars=letters[mid]
                end=mid-1
            else:
                start=mid+1
        return chars
