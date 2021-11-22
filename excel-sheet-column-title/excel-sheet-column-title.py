class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        apha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        output=""
        while (columnNumber!=0):
                add=columnNumber%26-1
                output=apha[add]+output
                columnNumber=(columnNumber-1)//26
        return output