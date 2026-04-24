class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_at = prices[0]
        curr = 0
        maxP = 0
        for i in range(1, len(prices)):
            if prices[i]<buy_at:
                buy_at = prices[i]
            else:
                currP = prices[i]-buy_at
                maxP = max(maxP, currP)
        return maxP    