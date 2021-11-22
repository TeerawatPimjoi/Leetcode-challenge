class Solution:
    def isHappy(self, n: int) -> bool:
        k=True
        urset=set()
        while(k==True):
            num = str(n)
            number=sum([int(c)**2 for c in num]) 
            n=number
            if n ==1 :
                k==True 
                break;
            if n in urset: 
                k=False
                break;
            urset.add(n)
        return k
            
            
            
        