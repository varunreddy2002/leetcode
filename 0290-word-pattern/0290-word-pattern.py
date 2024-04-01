class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        f=s.split(" ")
        if(len(set(pattern)) !=len(set(f))): return False
        for i in range(len(pattern)):
            d[pattern[i]]= f[i]

        t=""
        for i in pattern:
            t+=" "+d[i]
        t=t[1:]
        
        print(t)
        print(s)
        if(t==s):
            return True
        else:
            return False
            
            
        