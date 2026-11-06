class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re 
        # strs = s.replace(" ", "").lower()
        strs = re.sub(r'[^A-Za-z0-9]', '', s)
        strs=strs.lower()
        print(strs)
        n= len(strs)
        l=0
        r=n-1
        while r>=0 and l<n:
            if strs[l]!=strs[r]:
                return False
            l+=1
            r-=1
        return True
        