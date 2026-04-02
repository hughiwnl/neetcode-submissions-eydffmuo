class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(len(prices)):
            if prices[i] - buy > profit:
                profit = prices[i] - buy 
            if prices[i] < buy:
                buy = prices[i]
        return profit
        
        #return profit