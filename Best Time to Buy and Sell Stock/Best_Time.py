class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        # for i, price in enumerate(prices):
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profits = prices[sell] - prices[buy]
                sell += 1
                profit = max(profit, profits)
            else:
                buy = sell
                sell += 1
        return profit

        """
        :type prices: List[int]
        :rtype: int
        """
