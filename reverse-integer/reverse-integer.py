class Solution:
    def reverse(self, x: int) -> int:
        index=[]
        s,sub=0,0
        min,max=-2**31,2**31
        if x <0 : 
            x=x*-1
            sub=1
        while x>0:
            k=x%10
            index.append(k)
            x=x//10
        for i in range (0,len(index)):
            s+=index[i]*10**(len(index)-i-1)
        if sub==0 and min<s<max : return s
        if sub==1 and min<s<max: return -s
        return 0
        
            
            
            
        


            