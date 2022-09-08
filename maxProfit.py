class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left = 0
        profit = 0
        right = left + 1

        for i in range( 1, len( prices ) ):

            if prices[left] < prices[right]:
                profit = - (prices[left] - prices[right])
                maxP = max( maxP, profit )

            else:
                left = right
            right = right + 1

        return maxP

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# when you can buy lower why buy higher in the left hence there the left slider changes when right costs lower than left.
#and in any case its gonna step the right slider to right


