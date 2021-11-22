class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        urdict = {}
        if len(s)!=len(t) :return False
        for c in s :
            if c not in urdict : urdict[c]=1
            elif c in urdict : urdict[c]+=1
        
        for k in t:
            if k in urdict : urdict[k]-=1
        
        for value in urdict.values():
            if value >0: return False
        return True
        
        