class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}
        ss = s.lower()
        wordset=[e for e in ss if e in alpha]
        first =0
        last=len(wordset)-1
        ans=True
        while (first<last):
            if wordset[first]!=wordset[last]:
                ans=False
            first+=1
            last-=1
        return ans
        