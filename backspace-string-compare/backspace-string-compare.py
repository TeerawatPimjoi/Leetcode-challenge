class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks=[]
        stackt=[]
        for i in range (len(s)):
            if len(stacks)!=0 and s[i]=='#' :stacks.pop(-1)
            elif s[i]!="#":stacks.append(s[i])
        for i in range (len(t)):
            if len(stackt)!=0 and t[i]=='#' : stackt.pop(-1)
            elif t[i]!="#":stackt.append(t[i])  
        return stacks==stackt
    
        