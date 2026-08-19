class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        for i in range(len(prices)-1):
            j=len(prices)-1
            while j>i:
                profit=prices[j]-prices[i]
                if profit>maxProfit:
                    maxProfit=profit
                j-=1
        return maxProfit