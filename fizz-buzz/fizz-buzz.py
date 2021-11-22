class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        k= [str(e) for e in range(1,n+1)]
        for i in range (len(k)):
            if (i+1)%3==0  : k[i] = "Fizz"
            if (i+1)%5==0  : k[i] = "Buzz"
            if (i+1)%15==0  : k[i] = "FizzBuzz"
        return k
        
        