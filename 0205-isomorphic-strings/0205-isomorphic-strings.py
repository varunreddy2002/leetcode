class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(set(s))!=len(set(t))):
            return False
        d={}
        for i in range(len(s)):
            d[s[i]]=t[i]
        
        p=""
        for i in s:
            p+=d[i]
        if(p==t):
            return True
        return False
        