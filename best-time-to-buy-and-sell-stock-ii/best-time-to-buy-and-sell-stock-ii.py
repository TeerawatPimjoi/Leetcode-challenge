class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        difflist = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        plus = [e for e in difflist if e>0]
        ans = sum(plus)
        return ans

            