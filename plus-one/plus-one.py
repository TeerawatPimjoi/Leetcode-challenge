class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        need=[str(e) for e in digits ]
        number = int("".join(need))
        plus=str(number+1)
        plusone =[int(e) for e in plus]
        
        return plusone
        