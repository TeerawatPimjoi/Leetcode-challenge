class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        char ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s=0
        for i in range(len(columnTitle)):
            point=char.index(columnTitle[i])+1
            index = len(columnTitle)-1-i
            k= point*(26**index)
            s+=k
        return s
            